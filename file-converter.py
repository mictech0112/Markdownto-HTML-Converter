import os
import sys
import markdown

class MarkdownConverter:
    CMD = "markdown"

    @staticmethod
    def convert(arguments):
        if not MarkdownConverter.validate(arguments):
            return "Something went wrong..."

        input_file = arguments[2]
        output_file = arguments[3]

        print("Reading file...")
        with open(input_file) as f:
            contents = f.read()
        print("Finished reading file!!")

        html_contents = markdown.markdown(contents, extensions=['tables'])

        print("Converting file...")
        with open(output_file, 'w') as f:
            f.write(html_contents)
        print("Finished converting file!!")

        return "Done!!!"

    @staticmethod
    def validate(arguments):
        if len(arguments) != 4:
            return False

        if arguments[1] != MarkdownConverter.CMD:
            return False

        if not os.path.isfile(arguments[2]):
            return False

        if not MarkdownConverter.verify_output_path(arguments[3]):
            return False

        print("Validation succeeded!!")
        return True

    @staticmethod
    def verify_output_path(output_path):
        if os.path.isfile(output_path):
            user_input = input("The destination file already exists. Do you want to overwrite it? (y/N): ")
            if user_input.lower() != 'y':
                return False
        return True

if __name__ == "__main__":
    print(MarkdownConverter.convert(sys.argv))
