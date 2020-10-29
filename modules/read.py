def read_file(file_path: str):
    lines_list = []

    with open(file_path) as file:
        for line in file:
            lines_list.append(line)

    return lines_list


def extract_lines_by_indicator(lines_list, indicator):
    return [line for line in lines_list if str(line).startswith(indicator)]
