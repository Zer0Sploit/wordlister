import argparse

def generate_wordlist(org_name, source_wordlist, separator, only_separator):
    # Open the source wordlist file
    with open(source_wordlist, "r", encoding='ISO-8859-1') as f:
        words = f.readlines()

    custom_words = []

    # Generate custom wordlist with only the specified separator
    if only_separator:
        custom_words = [f"{org_name.capitalize()}{only_separator}{word.strip()}" for word in words] + \
                       [f"{org_name.lower()}{only_separator}{word.strip()}" for word in words] + \
                       [f"{org_name.upper()}{only_separator}{word.strip()}" for word in words]
    else:
        # Generate custom wordlist with the specified separator and default '@' and '' separators
        custom_words = [f"{org_name.capitalize()}{separator}{word.strip()}" for word in words] + \
                       [f"{org_name.lower()}{separator}{word.strip()}" for word in words] + \
                       [f"{org_name.upper()}{separator}{word.strip()}" for word in words] + \
                       [f"{org_name.capitalize()}@{word.strip()}" for word in words] + \
                       [f"{org_name.lower()}@{word.strip()}" for word in words] + \
                       [f"{org_name.upper()}@{word.strip()}" for word in words] + \
                       [f"{org_name.capitalize()}{word.strip()}" for word in words] + \
                       [f"{org_name.lower()}{word.strip()}" for word in words] + \
                       [f"{org_name.upper()}{word.strip()}" for word in words]

    # Write the custom wordlist to a file
    with open(f"{org_name}_wordlist.txt", "w") as f:
        f.writelines("\n".join(custom_words))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--org_name", required=True, help="Name of the organization")
    parser.add_argument("-w", "--wordlist", help="Path to the source wordlist")
    parser.add_argument("-s", "--separator", default="@", help="Separator character")
    parser.add_argument("-only", "--only_separator", help="Generate custom wordlist with only the specified separator")
    args = parser.parse_args()

    generate_wordlist(args.org_name, args.wordlist, args.separator, args.only_separator)
 
