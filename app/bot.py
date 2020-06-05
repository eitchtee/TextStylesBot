import logging
from uuid import uuid4

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, InlineQueryHandler, CommandHandler

from config import BOT_TOKEN
from text_generators import *

# from telegram.utils.helpers import escape_markdown

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - '
                           '%(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    # Send the message with menu
    update.message.reply_text("*Welcome to Text Fomatting Bot!*\n\n"
                              "Currently I only work via inline query, "
                              "on any conversation summon me using @txtfrmtbot"
                              ", type your message and choose the style you"
                              " want.\n\n"
                              "My code can be found [here]"
                              "(https://github.com/eitchtee/TextStylesBot).\n"
                              "Report any issue or suggestions [here]"
                              "(https://github.com/eitchtee/TextStylesBot/issues).\n\n"
                              "🤖 Hope you like me!",
                              parse_mode='Markdown',
                              disable_web_page_preview=True)


def inlinequery(bot, update):
    """Handle the inline query."""
    query = update.inline_query.query
    results = []

    if (not query):
        update.inline_query.answer(results)
        return

    zalgo_res = zalgo_txt(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Zalgo (Z̙͑͘a̵̺̳̫̅́́͋l̝̠͑̃͘͢ǵ̨͎̰͈͂͆̑ơ̳͚̳͒ W̹͛͝a̛͙̫̤͌ṋ͖̙̇ͧ̊͜ t͙ͮ̀̈́ͣ͞ͅsͭ̐ͥ͢͜ Ÿ̶͈́ͣ͋o̡͖̜͓͆̿ų̜͍͎͛͌̏ͨ)",
            description=zalgo_res,
            input_message_content=InputTextMessageContent(
                message_text=zalgo_res)))

    up_and_down_res = upper_and_lower(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Up and Down (bRoKeN cApSlOcK)",
            description=up_and_down_res,
            input_message_content=InputTextMessageContent(
                message_text=up_and_down_res)))

        # InlineQueryResultArticle(
        #     id=uuid4(),
        #     title="Binary",
        #     description="0s and 1s",
        #     input_message_content=InputTextMessageContent(
        #         message_text=binary(query))),

    double_struck_res = double_struck(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Double Struck (𝔽𝕒𝕟𝕔𝕪)",
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

    spaced_res = spaced(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Spaced (S P A C E D)",
            description=spaced_res,
            input_message_content=InputTextMessageContent(
                message_text=spaced_res)))

    circled_res = circled(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Circled (Ⓒⓘⓡⓒⓛⓔⓢ)",
            description=circled_res,
            input_message_content=InputTextMessageContent(
                message_text=circled_res)))

    negative_circled_res = negative_circled(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Filled Circled (🅒🅘🅡🅒🅛🅔🅢 🅑🅤🅣 🅕🅘🅛🅛🅔🅓)",
            description=negative_circled_res,
            input_message_content=InputTextMessageContent(
                message_text=negative_circled_res)))

    parenthesis_res = parenthesis(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Parenthesis [🄟⒜⒭⒠⒩⒯⒣⒠⒮⒤⒮]",
            description=parenthesis_res,
            input_message_content=InputTextMessageContent(
                message_text=parenthesis_res)))

    fraktur_res = fraktur(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Gothic (𝔊𝔬𝔱𝔥𝔦𝔠)",
            description=fraktur_res,
            input_message_content=InputTextMessageContent(
                message_text=fraktur_res)))

    leet_res = leet(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Leet Speak (1337, y0!)",
            description=leet_res,
            input_message_content=InputTextMessageContent(
                message_text=leet_res)))

    large_res = large(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Full-width (ＢＩＧ！)",
            description=large_res,
            input_message_content=InputTextMessageContent(
                message_text=large_res)))

    reverse_res = reverse(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Reversed (desreveR)",
            description=reverse_res,
            input_message_content=InputTextMessageContent(
                message_text=reverse_res)))

    morse_code_res = morse_code(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Morse Code (-- --- .-. ... .)",
            description=morse_code_res,
            input_message_content=InputTextMessageContent(
                message_text=morse_code_res)))

    strikethrough_res = strikethrough(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Strikethrough (̶̶S̶t̶r̶i̶k̶e̶t̶h̶r̶o̶u̶g̶h̶)",
            description=strikethrough_res,
            input_message_content=InputTextMessageContent(
                message_text=strikethrough_res)))

    small_caps_res = small_caps(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Small Caps (sᴍᴀʟʟ)",
            description=small_caps_res,
            input_message_content=InputTextMessageContent(
                message_text=small_caps_res)))

    superscript_res = superscript(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Superscript (Superˢᶜʳᶦᵖᵗ)",
            description=superscript_res,
            input_message_content=InputTextMessageContent(
                message_text=superscript_res)))

    underline_res = underline(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Underline (U̲n̲d̲e̲r̲l̲i̲n̲e̲)",
            description=underline_res,
            input_message_content=InputTextMessageContent(
                message_text=underline_res)))

        # InlineQueryResultArticle(
        #     id=uuid4(),
        #     title="Bold",
        #     description="*text*",
        #     input_message_content=InputTextMessageContent(
        #         message_text="*{}*".format(query),
        #         parse_mode=ParseMode.MARKDOWN)),
        # InlineQueryResultArticle(
        #     id=uuid4(),
        #     title="Italic",
        #     description="_text_",
        #     input_message_content=InputTextMessageContent(
        #         message_text="_{}_".format(query),
        #         parse_mode=ParseMode.MARKDOWN)),
        # InlineQueryResultArticle(
        #     id=uuid4(),
        #     title="Monospace",
        #     description="```text```",
        #     input_message_content=InputTextMessageContent(
        #         message_text="```{}```".format(query),
        #         parse_mode=ParseMode.MARKDOWN)),

    cebolinha_res = cebolinha(query)
    results.append(
        InlineQueryResultArticle(
            id=uuid4(),
            title="Cebolinha (Troque seu R por um L)",
            description=cebolinha_res,
            input_message_content=InputTextMessageContent(
                message_text=cebolinha_res)))

    update.inline_query.answer(results)


def error(bot, update, erro):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, erro)


def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(InlineQueryHandler(inlinequery))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
