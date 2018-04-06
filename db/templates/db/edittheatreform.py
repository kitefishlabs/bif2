#!/usr/bin/python

from editformtools import *

startPage("Theatre","theatre",requiredfields=["organization","work_samples_website","numberperformers","membersinfo","out_of_town","proposaloverlap","agesensitive"])
textInput("Performance title", "title")
textInput("Organization / production company", "organization")
textInput("Website (not Facebook)", "website")
textInput("Social media address(es)", "facebook", placeholder="facebook / instagram / twitter")
textInput("Web link to best example of what you plan to do", "work_samples_website", "a good link will answer most of our questions, to program you effectively")
textarea("Short description (140 chars)", "description_short", 2, placeholder="This is what people will see in the free weekly paper.  Limited to 140 characters; be succinct.")
textarea("Long description (for website &amp; press releases)", "description_long", 6, placeholder="This text will be shown publicly on our website.  This is what potential audiences see in the schedule on our site.")
textInput("How many members in proposal? (#)", "numberperformers")
textarea("Who are they and what do they do?", "membersinfo", 6)
textInput("Are you based within 60 miles of Buffalo area? Will you need help with housing?", "out_of_town")
textarea("Are any of your members in other proposals? Explain.", "proposaloverlap", 2)
yesnoInput("Is everyone in proposal over 21?", "over21")
yesnoInput("Would you like to be scheduled for outdoor performances (sidewalks, porches, yards, parking lots, etc)?", "outdoorperformaces")
menuInput("Where do prefer to be scheduled?", "street_preferred", ["all indoor", "mostly indoor", "either indoor or outdoor", "mostly outdoor", "all outdoor"])
menuInput("Desired number of performances", "numberperformances", [1,2,3,4,5])
yesnoInput("Do you want more than one performance per day?", "morethan1perday", default='n')
textInput("Length of performance: (in minutes)", "showlength")
yesnoInput("Is this flexible?", "showlengthflexible")
textInput("Setup time (in minutes)", "setuptime")
textInput("Teardown time (in minutes)", "teardowntime")
textInput("Do you have a prearranged venue?", "prearrangedvenue")
textInput("Do you have an ideal venue in mind?", "idealvenue")
textarea("What requirements do you have for your venue?", "venuerequirements")
textInput("Is the performance kid-friendly, or does it have age-sensitive content, or neither?", "agesensitive")
textInput("Proposal secondary categories, if any:", "secondary_category", placeholder="music, dance, visual art, literary, film/video, workshop")
yesnoInput("Are you interested in collaborating (performing in combination with another proposal of the same or different category)?", "collaboration", default='n')
textarea("If yes, describe the kinds of proposals that might work, and any other info to guide us.", "collaboration_details")
print("</table></div>")

availabilitySection()

print("<div class='projectForm'>\n<h3>Theatre specifics</h3>\n<table>\n")
textInput("Do you require audio amplification or playback (Y/N)? If so, please give details.", "audio")
textInput("Do you require chairs for the audience?", "chairs")
textInput("Does your proposal require a projector/screen?  If yes, explain.", "projector")
textInput("Does your proposal require a professional dance stage?", "dancestage")
textInput("Does your proposal require professional lighting?", "lighting")
textInput("Does your proposal require AC power?", "acpower")
textarea("Your equipment details (what equipment you bring, plus any unusual or unusually large setups)", "equipment")
genreMenu = [ "Dinner Theatre", "Musical", "Opera", "Revue", "Repertory Theatre", "Variety Show", "Vaudeville", "Drama", "Comedy", "Black Comedy", "Farce", "Improvisational Theatre", "Tragedy", "In-Your-Face Theatre", "Experimental (avant garde)", "Other" ]
menuInput("What genre best describes your act?", "genre", genreMenu)
menuInput("What other genre best describes your act?", "genre2", genreMenu)
menuInput("Ideally, we'd prefer:", "stagetype", [ "black box", "traditional stage", "alternative", "outdoor" ])
print("</table></div>")


print("<div class='projectForm'>\n<h3>Final details</h3>\n<table class='alternategrey'>\n")
textarea("In what ways are you willing to volunteer?", "volunteer", 2, placeholder="equipment gopher, tech (audio/video/stage/etc), PR distribution, videography/photography, other")
textInput("Anything else we need to know?", "anythingelse")
textInput("Any questions?", "questions")
print("</table></div>")

endPage()

