def format_name(full_name: str) -> str:
    parts = full_name.split()
    family, ism, sharif = parts[0], parts[1], " ".join(parts[2:])
    return f"{ism} {sharif}, {family}"

print(format_name("Aliyev Vali G'aniyevich"))
