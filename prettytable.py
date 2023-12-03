
def create_table(data):
    # Calculate the column amounts
    column_widths = [max([len(str(row[i])) for row in data]) for i in range(len(data[0]))]

    # Create top border
    table = "\n"+"+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+" + "\n"

    # Addheader row
    header = data[0]
    table += "|" + "|".join(
        [f" {header[i]} " + " " * (column_widths[i] - len(header[i])) for i in range(len(header))]) + "|" + "\n"

    # Add divider
    table += "+" + "+".join(["=" * (width + 2) for width in column_widths]) + "+" + "\n"

    # Add data rows
    for row in data[1:]:
        table += "|" + "|".join(
            [f" {row[i]} " + " " * (column_widths[i] - len(str(row[i]))) for i in range(len(row))]) + "|" + "\n"
        table += "" + "".join(["" * (width + 3) for width in column_widths]) + "" + "\n"

    # Remove last line divider
    table = table[:-1]

    # Add bottom border
    table += "+" + "+".join(["-" * (width + 2) for width in column_widths]) + "+"

    print(table)
