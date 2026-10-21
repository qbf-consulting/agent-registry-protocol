// Licensed under Apache-2.0.
// Informative repository-owned implementation experiment for ARPA Profile A.

#[derive(Debug, PartialEq, Eq)]
pub struct ResolutionDecision {
    pub outcome: &'static str,
    pub reason_code: &'static str,
}

/// Independently implements the observable identifier-resolution outcomes
/// exercised by ARPA Candidate v0.10.0 Profile A vectors TV-A-01..03.
///
/// This function does not confer authority. It distinguishes identifier
/// existence/lifecycle visibility only.
pub fn resolve_identifier(
    known: bool,
    terminal: bool,
    authorized_caller: bool,
) -> ResolutionDecision {
    if !known {
        return ResolutionDecision {
            outcome: "not_found",
            reason_code: "identifier_never_issued",
        };
    }
    if !authorized_caller {
        return ResolutionDecision {
            outcome: "not_authorized",
            reason_code: "caller_not_authorized_for_record",
        };
    }
    if terminal {
        return ResolutionDecision {
            outcome: "terminal_record",
            reason_code: "identifier_known_but_terminal",
        };
    }
    ResolutionDecision {
        outcome: "active_record",
        reason_code: "identifier_known_and_active",
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn known_active_identifier_resolves_active() {
        assert_eq!(
            resolve_identifier(true, false, true),
            ResolutionDecision {
                outcome: "active_record",
                reason_code: "identifier_known_and_active",
            }
        );
    }

    #[test]
    fn never_issued_identifier_resolves_not_found() {
        assert_eq!(
            resolve_identifier(false, false, true),
            ResolutionDecision {
                outcome: "not_found",
                reason_code: "identifier_never_issued",
            }
        );
    }

    #[test]
    fn terminal_identifier_is_not_masked_as_unknown() {
        assert_eq!(
            resolve_identifier(true, true, true),
            ResolutionDecision {
                outcome: "terminal_record",
                reason_code: "identifier_known_but_terminal",
            }
        );
    }

    #[test]
    fn unauthorized_known_identifier_is_not_disclosed() {
        assert_eq!(
            resolve_identifier(true, false, false),
            ResolutionDecision {
                outcome: "not_authorized",
                reason_code: "caller_not_authorized_for_record",
            }
        );
    }
}
