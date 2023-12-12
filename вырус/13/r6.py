def insert_spaces(line, target_length=80):
    words = line.split()
    if len(words) == 1:
        return line

    total_spaces = target_length - len(''.join(words))
    spaces_between_words = total_spaces // (max(len(words) - 1, 1))
    extra_spaces = total_spaces % max((len(words) - 1), 1)

    new_line = words[0]
    for i in range(1, len(words)):
        spaces = spaces_between_words + (1 if i <= extra_spaces else 0)
        new_line += ' ' * spaces + words[i]

    return new_line


def format_text(input_file, output_file):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    formatted_lines = [insert_spaces(line.strip()) for line in lines]

    with open(output_file, 'w') as outfile:
        outfile.write('\n'.join(formatted_lines))


# Приклад виклику функції для форматування тексту з файлу 'input.txt' та збереження результату у файл 'output.txt'
format_text('file_13_7', 'H')

