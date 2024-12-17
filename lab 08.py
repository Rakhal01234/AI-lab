unification using FOL

def occurs_in(var, term):
    """Check if a variable occurs within a term."""
    if var == term:
        return True
    elif isinstance(term, tuple):
        return any(occurs_in(var, subterm) for subterm in term)
    return False

def unify_term(psi1, psi2):
    """Unify two terms or predicates."""
    
    # Step 1: If Ψ1 or Ψ2 is a variable or constant, then:
    if isinstance(psi1, str) or isinstance(psi2, str):  # If either is a variable or constant
        if psi1 == psi2:  # a) If Ψ1 or Ψ2 are identical, return NIL
            return None
        elif isinstance(psi1, str):  # Ψ1 is a variable
            if occurs_in(psi1, psi2):  # a. If Ψ1 occurs in Ψ2, return FAILURE
                return "FAILURE"
            else:  # b. Else return { (Ψ2 / Ψ1) }
                return {psi1: psi2}
        elif isinstance(psi2, str):  # Ψ2 is a variable
            if occurs_in(psi2, psi1):  # a. If Ψ2 occurs in Ψ1, return FAILURE
                return "FAILURE"
            else:  # b. Else return { (Ψ1 / Ψ2) }
                return {psi2: psi1}
        else:  # Both are constants but different, return FAILURE
            return "FAILURE"

    # Step 2: If the initial predicate symbols are not the same, return FAILURE
    if isinstance(psi1, tuple) and isinstance(psi2, tuple):
        if psi1[0] != psi2[0]:  # Compare predicate symbols (first elements)
            return "FAILURE"

    # Step 3: If Ψ1 and Ψ2 have a different number of arguments, return FAILURE
    if len(psi1) != len(psi2):  # Different number of arguments
        return "FAILURE"

    # Step 4: Set the Substitution set(SUBST) to NIL (empty dictionary)
    subst = {}

    # Step 5: For each argument i in the predicates
    for i in range(1, len(psi1)):  # Ignore the predicate symbol itself (first element)
        s = unify_term(psi1[i], psi2[i])  # Call unify function for ith arguments
        
        if s == "FAILURE":  # If any unification fails
            return "FAILURE"
        
        if s is not None:  # If there is a substitution
            # Apply the substitution to the rest of the terms
            psi1 = apply_substitution(psi1, s)
            psi2 = apply_substitution(psi2, s)
            subst.update(s)  # Append the substitution

    # Step 6: Return the substitution set
    return subst

def apply_substitution(term, substitution):
    """Apply a substitution to a term (or predicate)."""
    if isinstance(term, str):  # If term is a variable, apply substitution
        return substitution.get(term, term)
    elif isinstance(term, tuple):  # If term is a tuple (predicate)
        return tuple(apply_substitution(subterm, substitution) for subterm in term)
    return term  # If it's a constant, no substitution

# Test the unification algorithm
def test_unification():
    # Example 1: Simple unification
    psi1 = ('father', 'john', 'mary')
    psi2 = ('father', 'X', 'mary')
    result = unify_term(psi1, psi2)
    print(f"Unification result for {psi1} and {psi2}: {result}")

    # Example 2: Unification with failure
    psi1 = ('father', 'john', 'mary')
    psi2 = ('mother', 'X', 'mary')
    result = unify_term(psi1, psi2)
    print(f"Unification result for {psi1} and {psi2}: {result}")

test_unification()
