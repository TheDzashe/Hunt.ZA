def is_valid(email)-> bool:
# case 1: look for more than one @
    if email.count("@") != 1:
        return False

    try:
        local_part, domain_part = email.split("@")
    except ValueError:
        return False

    #this should be security
    for char in [' ', '"', '(', ')', ',', ':', ';', '<', '>', '[', ']']:
        if char in local_part or char in domain_part:
            return False

# local part is empty
    if not local_part or not local_part.strip():
        return False

    if not domain_part or not domain_part.strip():
        return False

    if ".." in domain_part or domain_part.endswith("."):
        return False


# splitting email into labels 
    labels = domain_part.split(".")

    if len(labels) < 2:
        return False

    for label in labels:
        if len(label) == 0 or len(label) > 63:
            return False

        if label.startswith("-") or label.endswith("-"):
            return False
            
        if " " in label:
            return False
        
    tld = labels[-1]
    if len(tld) < 2 or tld.isdigit():
        return False

    return True
   




