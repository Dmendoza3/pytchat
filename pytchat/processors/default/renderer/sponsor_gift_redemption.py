from .base import BaseRenderer


class LiveChatSponsorshipsGiftRedemptionAnnouncementRenderer(BaseRenderer):
    def settype(self):
        self.chat.type = "sponsorGiftRedemption"
