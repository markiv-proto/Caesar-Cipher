import argparse
from pathlib import Path
from caesar.cipher import caesar_encrypt, caesar_decrypt, caesar_bruteforce

def main():
    parser = argparse.ArgumentParser(
        description="Caesar Cipher Encryption/Decryption Tool"
    )

    parser.add_argument(
        "mode",
        choices=["encrypt", "decrypt", "bruteforce"],
        help="Choose whether to encrypt, decrypt or bruteforce the text"
    )

    parser.add_argument(
        "--text",
        help="The input text to process"
    )

    parser.add_argument(
        "--shift",
        type=int,
        default=3,
        help="Shift value (default: 3)"
    )

    parser.add_argument(
        "--input",
        type = Path,
        help = "Path to input file"
    )

    parser.add_argument(
        "--output",
        type = Path,
        help = "Path to output file"
    )

    args = parser.parse_args()

    #Get input text from file or argument
    if args.input:
        text = args.input.read_text(encoding = "utf-8")
    elif args.text:
        text = args.text
    else:
        parser.error("You must provide either --text or --input file.")


    # Perform the operation
    if args.mode == "encrypt":
        result = caesar_encrypt(text, args.shift)
        output_label = "Encrypted Text"
    elif args.mode == "decrypt":
        result = caesar_decrypt(text, args.shift)
        output_label = "Decrypted Text"
    elif args.mode == "bruteforce":
        results = caesar_bruteforce(text)
        result = "\n".join([f"Shift {shift:2}: {txt}" for shift, txt in results.items()])
        output_label = "Bruteforce Results"

    #Print to console
    print(f"{output_label}:\n{result}")

    #Save to file or print
    if args.output:
        args.output.write_text(result, encoding="utf-8")
        print(f"Result written to {args.output}")

if __name__ == "__main__":
    main()
