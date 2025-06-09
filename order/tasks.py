# tasks.py
import aiohttp
import asyncio
from django.utils.html import escape

TELEGRAM_TOKEN = '7924154608:AAE-Fj_ClqvOL49qrqqQzx9DNuyxHheubtU'
CHAT_ID = ['658110617', '-1002368870625']

def format_price(num):
    # 1970000 -> "1 970 000"
    return f"{num:,}".replace(",", " ")

async def send_order_telegram_message_async(message: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "text": message,
        "parse_mode": "HTML"
    }

    async with aiohttp.ClientSession() as session:
        tasks = []
        for cid in CHAT_ID:
            data = {**payload, "chat_id": cid}
            tasks.append(session.post(url, data=data))
        try:
            await asyncio.gather(*tasks)
        except Exception as e:
            print(f"Ошибка при отправке в Telegram: {e}")

def send_order_telegram_message(order):
    items = order.items.all()
    product_lines = []

    for item in items:
        # Ограничиваем длину названия товара 20 символами
        product_name = escape(item.product_name)
        if len(product_name) > 50:
            product_name = product_name[:47] + "..."

        product_lines.append(
            f"🛍 <i>{product_name}</i>\n"
            f"💊 {escape(item.package_quantity)}\n"
            f"#️⃣ {item.quantity} × {format_price(int(item.price))} сум.\n"
            f"💸 {format_price(int(item.quantity)*int(item.price))} сум.\n"
        )

    total_price = sum([item.price * item.quantity for item in items])
    delivery_price = order.delivery_price or 0
    grand_total = total_price + delivery_price

    delivery_txt = (
        f"<b>🚛 Доставка:</b>\n {escape(order.delivery)}\n"
        f"<b>💸 Стоимость доставки:</b> {format_price(int(delivery_price))} сум.\n"
        if order.delivery != "Самовывоз из магазина" else "<b>Доставка:</b> Самовывоз из магазина"
    )

    message = f"""
<b>📢 Новый заказ</b>

👤 <b>Имя:</b> {escape(order.name)}
📞 <b>Телефон:</b> {escape(order.phone)}

🏠 <b>Адрес:</b>\n {escape(order.address) or '-'}
🖊️ <b>Комментарий:</b>\n {escape(order.comment) or '-'}

{delivery_txt}

<b>📦 Заказы:</b>\n
"""
    message += "\n".join(product_lines)
    message += f"\n\n<b>💸 Товары:</b> {format_price(int(total_price))} сум."
    message += f"\n<b>💰 Общая стоимость:</b>\n {format_price(int(grand_total))} сум."

    asyncio.run(send_order_telegram_message_async(message.strip()))
