from .base import BaseRenderer


class LiveChatMembershipItemRenderer(BaseRenderer):
    def settype(self):
        self.chat.type = "membershipMilestoneMessage"
