from aiogram import Router, F 
from aiogram.enums import ChatType
from aiogram.types import Message, KeyboardButton, KeyboardButtonRequestChat, KeyboardButtonRequestUser
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router()

router.message.filter(F.chat.type == ChatType.PRIVATE)

def keyboard_():
    kb = ReplyKeyboardBuilder()
    
    kb.row(
        KeyboardButton(text="👤 Пользователь", request_user=KeyboardButtonRequestUser(request_id=1))
    )
    
    kb.row(KeyboardButton(
                text="📰 Группа", 
                request_chat=KeyboardButtonRequestChat(request_id=2, chat_is_channel=False)
                        ), 
           KeyboardButton(
               text="📣 Канал", 
               request_chat=KeyboardButtonRequestChat(request_id=3, chat_is_channel=True))
    )
    
    return kb.as_markup()
    
@router.message(F.user_shared)
async def on_user_shared(m: Message):
    await m.reply(f"👤: USER ID ➔  <code>{m.user_shared.user_id}</code>")

@router.message(F.chat_shared)
async def on_user_shared(m: Message):
    await m.reply(f"📝: {'GROUP' if m.chat_shared.request_id == 2 else 'CHANNEL'} ID ➔  <code>{m.chat_shared.chat_id}</code>")
    
@router.message()
async def spam_checking(m: Message):
    await m.reply("<b>🎀 Получите идентификатор пользователя, канала или группы.</b>\n"
                   "🔘 Нажмите на кнопку, выберите и отправьте нужный чат.", reply_markup=keyboard_())