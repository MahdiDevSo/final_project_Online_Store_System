from models.store import Product

FILE_PATH = "data/products.txt"


def save_products(products: list[Product]):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write("# id|name|price|stock\n")
        for p in products:
            f.write(f"{p.id}|{p.name}|{p.price}|{p.stock}\n")


def load_products() -> list[Product]:
    products = []

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                parts = line.split("|")
                if len(parts) != 4:
                    continue

                products.append(
                    Product(
                        int(parts[0]),
                        parts[1],
                        float(parts[2]),
                        int(parts[3])
                    )
                )

    except FileNotFoundError:
        pass

    return products
