import logging
from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent, \
    ParseMode
from telegram.ext import Updater, InlineQueryHandler, CommandHandler

from config import BOT_TOKEN
from text_generators import *

# from telegram.utils.helpers import escape_markdown

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - '
                           '%(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update, context):
    # Send the message with menu
    update.message.reply_text("*Welcome to Text Fomatting Bot!*\n\n"
                              "Currently I only work via inline query, "
                              "on any conversation summon me using @txtfrmtbot"
                              ", type your message and choose the style you"
                              " want.\n\n"
                              "My code can be found [here]"
                              "(https://github.com/eitchtee/TextStylesBot).\n"
                              "Report any issue or suggestions [here]"
                              "(https://github.com/eitchtee/TextStylesBot"
                              "/issues).\n\n "
                              "🤖 Hope you like me!",
                              parse_mode='Markdown',
                              disable_web_page_preview=True)


def inlinequery(update, context):
    """Handle the inline query."""
    query = update.inline_query.query
    results = []

    if not query:
        update.inline_query.answer(results)
        return

    # Z̙͑͘a̵̺̳̫̅́́͋l̝̠͑̃͘͢ǵ̨͎̰͈͂͆̑ơ̳͚̳͒
    zalgo_res = zalgo_txt(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Zalgo",
            description=zalgo_res,
            input_message_content=InputTextMessageContent(
                message_text=zalgo_res)))

    # bRoKeN cApSlOcK
    up_and_down_res = upper_and_lower(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Up and Down",
            description=up_and_down_res,
            input_message_content=InputTextMessageContent(
                message_text=up_and_down_res)))

    # InlineQueryResultArticle(
    #     id=uuid4(),
    #     title="Binary",
    #     description="0s and 1s",
    #     input_message_content=InputTextMessageContent(
    #         message_text=binary(query))),

    # 𝔽𝕒𝕟𝕔𝕪
    double_struck_res = double_struck(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Double Struck",
            description=double_struck_res,
            input_message_content=InputTextMessageContent(
                message_text=double_struck_res)))

    cursive_res = cursive(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Cursive (𝓐𝓵𝓼𝓸 𝓯𝓪𝓷𝓬𝔂)",
            description=cursive_res,
            input_message_content=InputTextMessageContent(
                message_text=cursive_res)))

    # S P A C E D
    spaced_res = spaced(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Spaced",
            description=spaced_res,
            input_message_content=InputTextMessageContent(
                message_text=spaced_res)))

    # Ⓒⓘⓡⓒⓛⓔⓢ
    circled_res = circled(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Circled",
            description=circled_res,
            input_message_content=InputTextMessageContent(
                message_text=circled_res)))

    # 🅒🅘🅡🅒🅛🅔🅢 🅑🅤🅣 🅕🅘🅛🅛🅔🅓
    negative_circled_res = negative_circled(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Filled Circled",
            description=negative_circled_res,
            input_message_content=InputTextMessageContent(
                message_text=negative_circled_res)))

    # 🄟⒜⒭⒠⒩⒯⒣⒠⒮⒤⒮
    parenthesis_res = parenthesis(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Parenthesis",
            description=parenthesis_res,
            input_message_content=InputTextMessageContent(
                message_text=parenthesis_res)))

    # 𝔊𝔬𝔱𝔥𝔦𝔠
    fraktur_res = fraktur(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Gothic",
            description=fraktur_res,
            input_message_content=InputTextMessageContent(
                message_text=fraktur_res)))

    # 1337, y0!
    leet_res = leet(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Leet Speak",
            description=leet_res,
            input_message_content=InputTextMessageContent(
                message_text=leet_res)))

    # ＢＩＧ！
    large_res = large(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Full-width",
            description=large_res,
            input_message_content=InputTextMessageContent(
                message_text=large_res)))

    # desreveR
    reverse_res = reverse(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Reversed",
            description=reverse_res,
            input_message_content=InputTextMessageContent(
                message_text=reverse_res)))

    # -- --- .-. ... .
    morse_code_res = morse_code(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Morse Code",
            description=morse_code_res,
            input_message_content=InputTextMessageContent(
                message_text=morse_code_res)))

    # ̶S̶t̶r̶i̶k̶e̶t̶h̶r̶o̶u̶g̶h
    strikethrough_res = strikethrough(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Strikethrough",
            description=strikethrough_res,
            input_message_content=InputTextMessageContent(
                message_text=strikethrough_res)))

    # sᴍᴀʟʟ
    small_caps_res = small_caps(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Small Caps",
            description=small_caps_res,
            input_message_content=InputTextMessageContent(
                message_text=small_caps_res)))

    # Superˢᶜʳᶦᵖᵗ
    superscript_res = superscript(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Superscript",
            description=superscript_res,
            input_message_content=InputTextMessageContent(
                message_text=superscript_res)))

    # U̲n̲d̲e̲r̲l̲i̲n̲e̲
    underline_res = underline(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Underline",
            description=underline_res,
            input_message_content=InputTextMessageContent(
                message_text=underline_res)))

    bold_res = "*{}*".format(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Bold",
            description=bold_res,
            input_message_content=InputTextMessageContent(
                message_text=bold_res,
                parse_mode=ParseMode.MARKDOWN))
    )

    italic_res = "_{}_".format(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Italic",
            description=italic_res,
            input_message_content=InputTextMessageContent(
                message_text=italic_res,
                parse_mode=ParseMode.MARKDOWN)),
    )

    monospace_res = "`{}`".format(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Monospace",
            description=monospace_res,
            input_message_content=InputTextMessageContent(
                message_text=monospace_res,
                parse_mode=ParseMode.MARKDOWN)),
    )

    # Troque seu R por um L
    cebolinha_res = cebolinha(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Cebolinha",
            description=cebolinha_res,
            input_message_content=InputTextMessageContent(
                message_text=cebolinha_res)))

    update.inline_query.answer(results)


def error_callback(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(InlineQueryHandler(inlinequery))

    # log all errors
    dp.add_error_handler(error_callback)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
