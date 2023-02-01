# Wordlister
Wordlister generates a custom wordlist based on the specified organization name and source wordlist. The custom wordlist contains combinations of the organization name with each word from the source wordlist and a specified separator character.

# Usage

`python3 wordlister.py -n ORG_NAME -w SOURCE_WORDLIST -s SEPARATOR [-only ONLY_SEPARATOR]`

# Options

```
-n ORG_NAME, --org_name ORG_NAME
    Required. Name of the organization.

-w SOURCE_WORDLIST, --wordlist SOURCE_WORDLIST
    Path to the source wordlist.

-s SEPARATOR, --separator SEPARATOR
    Separator character. Default is "@".

-only ONLY_SEPARATOR, --only_separator ONLY_SEPARATOR
    Generate custom wordlist with only the specified separator.

```

# Example

`python wordlister.py -n tesla -w rockyou.txt -s "_"`

- This will generate a custom wordlist with the organization name "ExampleCorp" and the source wordlist "source_wordlist.txt", using the separator "_". The custom wordlist will be saved as "ExampleCorp_wordlist.txt"
