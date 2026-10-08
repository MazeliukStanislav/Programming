# База даних товарів: [id, назва, ціна, кількість_на_складі]
catalog = [
    {"id": 1, "name": "Ноутбук", "price": 25999.50, "stock": 5},
    {"id": 2, "name": "Мишка бездротова", "price": 450.00, "stock": 12},
    {"id": 3, "name": "Клавіатура", "price": 1200.80, "stock": 8},
    {"id": 4, "name": "Навушники", "price": 850.25, "stock": 3},
    {"id": 5, "name": "Монітор", "price": 6400.00, "stock": 4}
]

# Пароль для входу в режим адміністратора
ADMIN_PASSWORD = "admin"

# Кошик користувача: список обраних товарів
cart = []

# --- ЛЯМБДА-ФУНКЦІЇ ---
# Форматування ціни у вигляд "ххх.ххгрн"
format_price = lambda price: f"{price:.2f}грн"

# Пошук товару за ID
find_item = lambda item_id, items_list: next((item for item in items_list if item["id"] == item_id), None)

# Обчислення загальної суми кошика
calculate_total = lambda cart_items: sum(item["price"] for item in cart_items)


def show_catalog():
    print("\n--- КАТАЛОГ ТОВАРІВ ---")
    for item in catalog:
        status = "В наявності" if item["stock"] > 0 else "Немає в наявності"
        print(f"[{item['id']}] {item['name']} — {format_price(item['price'])} ({status}: {item['stock']} шт.)")


def add_to_cart():
    show_catalog()
    try:
        item_id = int(input("\nВведіть ID товару для додавання в кошик: "))
        item = find_item(item_id, catalog)

        if not item:
            print("Товар з таким ID не знайдено!")
            return

        if item["stock"] <= 0:
            print("На жаль, товару немає в наявності.")
            return

        # Зменшуємо залишок на складі та додаємо в кошик
        item["stock"] -= 1
        cart.append(item)
        print(f"Товар '{item['name']}' додано до кошика!")
    except ValueError:
        print("Помилка: Введіть коректний номер ID.")


def show_cart():
    print("\n--- ВАШ КОШИК ---")
    if not cart:
        print("Кошик порожній.")
        return False

    for idx, item in enumerate(cart, 1):
        print(f"{idx}. {item['name']} — {format_price(item['price'])}")

    total = calculate_total(cart)
    print(f"Загальна вартість: {format_price(total)}")
    return True


def remove_from_cart():
    if not show_cart():
        return

    try:
        idx = int(input("\nВведіть номер товару в кошику, який хочете видалити: ")) - 1
        if 0 <= idx < len(cart):
            removed_item = cart.pop(idx)
            # Повертаємо товар на склад
            removed_item["stock"] += 1
            print(f"Товар '{removed_item['name']}' видалено з кошика!")
        else:
            print("Некоректний номер товару.")
    except ValueError:
        print("Помилка: Введіть число.")


def checkout():
    if not cart:
        print("\nКошик порожній. Немає чого купувати!")
        return

    total = calculate_total(cart)
    print("\n--- ОФОРМЛЕННЯ ПОКУПКИ ---")
    print(f"Ви придбали товарів на суму: {format_price(total)}")
    cart.clear()
    print("Дякуємо за покупку!")


def admin_panel():
    password = input("Введіть пароль адміністратора: ").strip()
    if password != ADMIN_PASSWORD:
        print("Невірний пароль!")
        return

    print("\n=== ПАНЕЛЬ АДМІНІСТРАТОРА (ЗАЛИШКИ НА СКЛАДІ) ===")
    # Використання лямбди для перевірки критичних залишків
    is_low_stock = lambda stock: "⚠️ (Мало!)" if stock < 5 else ""

    for item in catalog:
        print(
            f"ID: {item['id']} | Назва: {item['name']:<20} | Ціна: {format_price(item['price']):<12} | Залишок: {item['stock']} шт. {is_low_stock(item['stock'])}")


def main():
    while True:
        print("\n==============================")
        print("      ГОЛОВНЕ МЕНЮ МАЗИНИ     ")
        print("==============================")
        print("1. Переглянути каталог товарів")
        print("2. Переглянути кошик")
        print("3. Додати товар в кошик")
        print("4. Видалити товар з кошика")
        print("5. Купити товари з кошика")
        print("6. Увійти як Адміністратор")
        print("0. Вийти з програми")

        choice = input("\nОберіть дію (0-6): ").strip()

        if choice == "1":
            show_catalog()
        elif choice == "2":
            show_cart()
        elif choice == "3":
            add_to_cart()
        elif choice == "4":
            remove_from_cart()
        elif choice == "5":
            checkout()
        elif choice == "6":
            admin_panel()
        elif choice == "0":
            print("\nДякуємо за користування програмою! До побачення.")
            break
        else:
            print("\nНекоректний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
