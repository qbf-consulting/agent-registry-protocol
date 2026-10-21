// Licensed under Apache-2.0.

use arpa_rust_identifier_resolution::resolve_identifier;
use std::env;
use std::process;

fn parse_bool(value: &str, name: &str) -> bool {
    match value {
        "true" => true,
        "false" => false,
        _ => {
            eprintln!("{name} must be true or false");
            process::exit(2);
        }
    }
}

fn main() {
    let mut known = false;
    let mut terminal = false;
    let mut authorized_caller = true;
    let args: Vec<String> = env::args().skip(1).collect();
    let mut index = 0;

    while index < args.len() {
        let flag = &args[index];
        let value = args.get(index + 1).unwrap_or_else(|| {
            eprintln!("missing value for {flag}");
            process::exit(2);
        });
        match flag.as_str() {
            "--known" => known = parse_bool(value, "--known"),
            "--terminal" => terminal = parse_bool(value, "--terminal"),
            "--authorized-caller" => {
                authorized_caller = parse_bool(value, "--authorized-caller")
            }
            _ => {
                eprintln!("unsupported argument: {flag}");
                process::exit(2);
            }
        }
        index += 2;
    }

    let decision = resolve_identifier(known, terminal, authorized_caller);
    println!(
        "{{\"outcome\":\"{}\",\"reason_codes\":[\"{}\"]}}",
        decision.outcome, decision.reason_code
    );
}
