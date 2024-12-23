import json
import os
from tkinter import mainloop

from groq import Groq
from dotenv import load_dotenv
load_dotenv(verbose=True)


article_content ={
                "uri": "2024-12-577693303",
                "lang": "eng",
                "isDuplicate": False,
                "date": "2024-12-16",
                "time": "19:40:36",
                "dateTime": "2024-12-16T19:40:36Z",
                "dateTimePub": "2024-12-16T19:39:51Z",
                "dataType": "news",
                "sim": 0,
                "url": "https://www.infowars.com/posts/a-vexed-question",
                "title": "A Vexed Question",
                "body": "The who, what, where, why and how of demographic change are vexed questions. The who, in particular, and the why.\n\nFor some, like Renaud Camus, the man who actually coined the term \"the Great Replacement,\" mass demographic change in the West is not the product of any kind of conspiracy. There is no \"who\" as such directing the importation of hordes of Third World people into the nations of Europe, North America and the Anglosphere.\n\nInstead, for Camus, the Great Replacement is simply the result of the spread of a way of thinking he terms \"replaceism\": a belief that, ultimately, all people are just interchangeable and therefore there is no such thing as, say, genuine national or ethnic identity that should or even could be preserved.\n\nWe might call a variant of this the \"magic soil\" theory of identity. There is nothing, nothing apart from an official legal process, that can stop a Nigerian who lands in France or the UK from becoming French or British or Welsh or even, like me, Cornish.\n\nCamus sees \"replaceism\" as emerging and growing due to the profound social, economic and spiritual changes of the modern era -- everything from the Reformation and the Enlightenment to the spread of industrialisation, capitalism, mass democracy, mass education and mass entertainment.\n\nThe television is as much to blame as any politician.\n\nThe \"why\" that follows from this de-centered \"who\" is clearly also de-centered. \"Replaceism\" is the logic of the modern liberal world. It's unavoidable. There isn't any malice behind it. It has terrible effects, of course, and it's destroying the West, but the will behind it is blind and unfeeling.\n\nIt's not personal, however much you might hate it.\n\nMany people who criticize or f\u00eate Camus don't actually seem to know this: that he identifies no single group that is to blame, even if he holds politicians and the media in deep contempt -- as he, and we, should -- for their cowardice and self-serving behaviour. People who describe Camus as a racist or white supremacist or even right wing usually tend to ignore what he's actually saying.\n\nThe opposite tendency -- well, we know what that looks like, don't we? An identifiable group and a clear sense of malice towards the people of the West. Often, that group is said to be some tribe of wandering desert folk, like the Bedouin or the Bakhtiari nomads of Iran. These people, from a deep historical antipathy for settled agricultural peoples and in particular Christians, have decided to subvert and overthrow their societies and civilisation from within.\n\nThis account, by contrast, is very personal.\n\nEverywhere we look, at all the institutions that are bringing on the Great Replacement -- from the government departments and the think-tanks to the religious NGOs bussing migrants and the universities indoctrinating Westerners to hate themselves, their culture and their history, not to mention the companies sapping the younger generation's desire to reproduce with porn, dating apps and parasocial smut websites like OnlyFans -- everywhere we look we detect the sandy fingers and the mint-yoghurt smell of a Bedouin or some such. Or so the theory goes.\n\nThe implication, of course, is that any attempt to reverse mass immigration and mass demographic change must therefore focus on this group primarily, on dislodging them from their secret control of the West.\n\nThe truth, I think, is somewhere in between. We absolutely must reckon with enormous impersonal changes that have taken place and made it possible to think a Nigerian can become a Briton simply on the basis of a citizenship test. The way we think about nationality and identity has changed tremendously, and it has changed tremendously over a long span of time, centuries in fact, without any obvious direction except its own inner logic, which draws its sources, as Camus shows, from many different places and things.\n\nAt the same time, though, we should also be alive to the genuine malice and wilfulness that seem to motivate official policies of mass immigration in Western nations.\n\nAs a Brit, I well remember the shocking revelations made by Andrew Neather, a former advisor to Tony Blair's New Labour government, which was responsible for introducing mass immigration to Britain beginning in 1997. In about 2010, Neather told a British newspaper that the policy had been specifically formulated to \"rub the right's nose in diversity\" and change the social fabric of Britain forever, so that a truly conservative government could never again be elected.\n\nThere was outcry at the time, and official denials, but why would Neather have made it up? He was simply being honest. Peter Mandelson, a New Labour grandee, said the government actually sent search parties out to Eastern Europe to get people to come to the UK, despite the fact they weren't really needed to fill jobs in the economy.\n\nIf you're an American, or even an observer from the other side of the Pond like me, it's hard to look at what happened in Springfield, Ohio or Charleroi, Pennsylvania or across the entire nation since 2021 and not see a deliberate plan to displace real Americans with foreigners, for political purposes (winning the election) at the very least.\n\nBut there's malice too, no doubt. The absurd, grotesque spectacle of 20,000 cat-eating Haitians being dumped in a small Midwest town bespeaks, to me, a deep hatred of actual Americans that is confirmed by everything else the Biden admin has done for the last four years.\n\nAnyway, I say all of this as a long prelude to the following observation, or rather question: Why is it that, as demographic replacement really begins to bite across the West, governments are so keen to bring in euthanasia services that will only be used by the natives?\n\nFrom the outside, it certainly looks like an evil twist to me, but could it just be happenstance.\n\nWith the release of the latest figures from Canada, which has gone turbo-Great Replacement under its oleaginous Prime Minister Justin Trudeau, we do at least know that this is the case: that white people are the overwhelming constituency for legal euthanasia.\n\n\"Medically assisted dying\" or \"MAiD\" is used almost entirely by white Canadians. Ninety-six percent of cases are white Canadians. White Canadians make up 67% of the population.\n\nCanadian doctors are now killing 15,000 people a year, more or less all of them white. That's 5% of all deaths in a given year. Many of these people are poor and ill, abandoned by a government and a welfare system that are only too happy to accommodate people with no ties whatsoever to Canada -- to house, feed, employ and care for their health, on the basis of no prior relationship at all.\n\nSome of those who seek MAiD are even veterans who have served Canada in the military. Instead of being offered wheelchair ramps for their homes and new prosthetics, they're offered a lethal injection.\n\nIf other Western countries that have legalised euthanasia -- Austria, the Netherlands, Spain, Belgium -- released statistics by ethnicity, I'm sure exactly the same pattern would be visible, just as starkly.\n\nAnd it's not just older people either. As we know from the case of Shanti de Corte or more recently the Belgian woman known only as \"Laura,\" it's young people too. Young people who despair at the state of the world and their countries, whether they know the real reasons for their despair or not. Shanti de Corte suffered PTSD after surviving an Islamist terror attack in Brussels.\n\nTo tell you the truth, I'm not sure what to make of this. But I do know it troubles me deeply. Malice or impersonal logic -- either way, it amounts to the same thing, and it's not good.",
                "source": {
                    "uri": "infowars.com",
                    "dataType": "news",
                    "title": "Infowars"
                },
                "authors": [],
                "image": "https://imagedelivery.net/aeJ6ID7yrMczwy3WKNnwxg/13c3d4ef-8b2b-4709-064c-1ff94dbfb800/w=800,h=450",
                "eventUri": None,
                "sentiment": 0.09019607843137245,
                "wgt": 92768,
                "relevance": 1
            }

# Send the article content for analysis
def post_groq_api(article_content: dict) -> dict:
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content":  (
                    f"{json.dumps(article_content)}\n\n"
                    "This is an article. I want to analyze a few things:\n"
                    "1. In what country did it happen?\n"
                    "2. Classify the article into one of the following categories: general news, historical terror attack, or nowadays terror attack.\n\n"
                    "After analyzing, provide a JSON with the following structure:\n"
                    "{\n"
                    "    \"category\": \"str\",\n"
                    "    \"country\": \"str\",\n"
                    "    \"city\": \"str\",\n"
                    "    \"continent\": \"str\",\n"
                    "    \"country_longitude\": \"int\",\n"
                    "    \"country_latitude\": \"int\",\n"
                    "}\n\n"
                    "Respond with the JSON only, without any extra text."
                ),
            }
        ],
        model="llama3-8b-8192",
    )
    return json.loads(chat_completion.choices[0].message.content)
# Extract and print the result
if __name__ == '__main__':
    print(post_groq_api(article_content))
