from .base import BaseRenderer


class LiveChatSponsorshipsGiftPurchaseAnnouncementRenderer(BaseRenderer):
    def settype(self):
        self.chat.type = "sponsorGift"

    def get_message(self, item):
        message = ''
        message_ex = []
        runs = item.get("header", {}).get("liveChatSponsorshipsHeaderRenderer", {}).get("primaryText", {}).get("runs", {})

        for r in runs:
            if not hasattr(r, "get"):
                continue
            if r.get('emoji'):
                message += r['emoji'].get('shortcuts', [''])[0]
                message_ex.append({
                    'id': r['emoji'].get('emojiId').split('/')[-1],
                    'txt': r['emoji'].get('shortcuts', [''])[0],
                    'url': r['emoji']['image']['thumbnails'][0].get('url')
                })
            else:
                message += r.get('text', '')
                message_ex.append(r.get('text', ''))

        self.chat.amountValue = message_ex[1]
        self.chat.amountString = message_ex[1]
        return message, message_ex


        return message, [message]
