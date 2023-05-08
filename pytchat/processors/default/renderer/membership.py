from .base import BaseRenderer


class LiveChatMembershipItemRenderer(BaseRenderer):
    def settype(self):
        self.chat.type = "newSponsor"

    def get_authordetails(self):
        super().get_authordetails()
        self.chat.author.isChatSponsor = True

    def get_message(self, item):
        try:
            #print("headerPrimaryText", item["headerPrimaryText"])
            if item.get("headerPrimaryText", -1) != -1:
                self.chat.type = "milestoneMessage"

                message = ''.join([mes.get("text", "")
                           for mes in item["headerPrimaryText"]["runs"]])
                
                message += "|" + item["headerSubtext"]["simpleText"] + "|"
                
                runs = item.get("message", {}).get("runs", {})
                for r in runs:
                    if not hasattr(r, "get"):
                        continue
                    if r.get('emoji'):
                        message += r['emoji'].get('shortcuts', [''])[0]
                    else:
                        message += r.get('text', '')
            else:
                message = ''.join([mes.get("text", "")
                           for mes in item["headerSubtext"]["runs"]])
        except KeyError as e:
            print(e)
            return "Welcome New Member!", ["Welcome New Member!"]
        return message, [message]
