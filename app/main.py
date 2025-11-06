def copy_file(command: str) -> None:
    command_list = command.split(" ")
    if len(command_list) < 3 or command_list[0] != "cp":
        return

    try:
        with open(command_list[1], mode="r") as file_read:
            file_data = file_read.read()

        with open(command_list[2], mode="w") as file_write:
            file_write.write(file_data)
    except FileNotFoundError:
        return
