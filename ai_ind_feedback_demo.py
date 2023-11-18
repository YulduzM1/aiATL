import vertexai
from vertexai.language_models import TextGenerationModel

vertexai.init(project="optical-highway-405503", location="us-central1")
parameters = {
    "candidate_count": 1,
    "max_output_tokens": 1024,
    "temperature": 0.2,
    "top_p": 0.8,
    "top_k": 40
}
model = TextGenerationModel.from_pretrained("text-bison")
response = model.predict(
    """You are a grader for grade 6-12 students who are writing essays. You will first need to segment each essay into discrete rhetorical and argumentative elements (i.e., discourse elements) and then classify each element as one of the following and most importantly, give feedback on what the essay is missing or does poorly

    Lead - an introduction that begins with a statistic, a quotation, a description, or some other device to grab the reader’s attention and point toward the thesis
    Position - an opinion or conclusion on the main question
    Claim - a claim that supports the position
    Counterclaim - a claim that refutes another claim or gives an opposing reason to the position
    Rebuttal - a claim that refutes a counterclaim
    Evidence - ideas or examples that support claims, counterclaims, or rebuttals.
    Concluding Statement - a concluding statement that restates the claims

input: Cell phones haven\'t been around a long time but they have become a very big part of our daily lives. Phones have went from something you use to just call people, too your very personal computer, up to date will all the new software to make surfing the internet easier. Now, that sounds wonderful but these thing can also so be a huge distraction to many. Especially when they are being used while operating a motor vehicle.

For one thing, using your cell phone causes many distractions for your eyes, your mind, and your actions. It is easily possible for your eyes tom slip off the road. The Tampa Bay Times claim that it \"takes seconds to get your eyes off the road and into a car accident\". Therefore, instead of your eyes being locked into your phone, they should be focusing in on your speed, the road, and the traffic. At the same time, your mind can only process so much. According to Goldsborough \"the human mind is not capable of texting and driving\". Other people have also confirmed that \" driving is a one mind chore\" meaning that the mind cannot to both at the same time. In addition, your mind need to focus on one thing while driving and that is the road. Thus, concentration is important while driving and breaking that concentration causes a risk for an accident.

Secondly, texting while driving not only endangers yourself but other people on the road as well. Texting while driving can limit your response time to something like a car pulling out in front of you, a child or adult walking in front of you, and other things. Texting someone means that you have to put all of your attention into what you are texting which, so if you are driving and texting at the same time you are bound to miss something that you should have been paying attention too or you can hit something that you should have been paying attention too, like a car, animal or even worse a person. A article called \"Texting While Driving\" states that texting and driving has become a \"prominent social issue, and it\'s the most hazardous practice that risks accidents to drivers, cyclists and pedestrians\". A pedestrian can walk onto the road at anytime but it is up to the driver to pay attention to road and avoid endangering his/her and the pedestrian life.

Finally, the numbers speak for themselves, too many accidents have occurred as a result of people texting and driving. People\'s lives will always be endangered if people feel like the best time to call their mom or girlfriend is when they are driving. If we can just wait until we arrive at our destination before having to pick up the phone while driving then we can avoid a lot more accidents and more lives will be spared. Remember, think before you pull out your phone to text someone while driving because life is to precious and short enough already.   Imagine having a Facial Coding System computers that identify\'s yours or your classmates emotions. How would you feel about having this system in your classroom? Would it be weird? Would it be fun and intersting?
output: Lead: The introduction lacks a specific statistic, quotation, or attention-grabbing device. Consider incorporating a compelling element to draw the reader\'s attention and point towards the thesis.

Position: The main position is implied but not explicitly stated. Clearly articulate the opinion or conclusion on the impact of cell phones, particularly when used while driving.

Claim:Claim 1: Distractions for Eyes, Mind, and Actions:
The claim is supported with mention of potential distractions for eyes and the mind. Consider reinforcing this claim with specific examples or statistics for greater impact.
Claim 2: Endangering Others on the Road:
This claim is well-supported with examples of how texting while driving can limit response time and pose risks to pedestrians, cyclists, and other drivers.
Claim 3: Too Many Accidents Occur due to Texting and Driving:
This claim is strongly supported with the assertion that too many accidents have occurred. Consider providing specific statistics to enhance the persuasiveness.

Counterclaims and Rebuttals:
The essay lacks explicit counterclaims and rebuttals. Addressing potential counterarguments would strengthen the overall argument.

Evidence:The essay provides some evidence, such as quotes from sources like the Tampa Bay Times and Goldsborough. Incorporating additional statistics or real-life examples would enhance persuasiveness.

Concluding Statement: The essay includes a concluding statement that emphasizes the importance of avoiding distractions while driving. It provides a call to action, encouraging readers to think before using their phones while driving.

input: Today, many people both own and operate cell phones on a daily basis. So much so, that many have developed the tendency to do so while operating a vehicle. This current trend of behavior among drivers has caused a series of debates as to whether or not one should be allowed to use their phone while driving. Due to the many risks that come with a distracted driver. Thus, why drivers should not be allowed to operate cell phones while operating a vehicle.

While operating a vehicle, it is important for drivers to stay focused on the road. However, cell phones are one of the most common causes of distracted driving related accidents. (The Most Common Causes of Distracted Driving). According to 4 Reasons Why You Shouldn\'t Text and Drive by B City of Bryan, \"Five seconds is the minimal amount of time your attention is taken away from the road when you\'re texting and driving.\" In addition, it generally only takes a driver about five seconds to travel the length of a football field when traveling around 55mph. This means that when drivers become distracted by their cell phones, they create a large window of opportunity for disaster to strike.

In most cases, people think that they can keep their eyes on the road while operating their cell phone at the same time. In contrast, drivers who allow themselves to get distracted by their cell phones increase their chances of getting into an accident, as well as putting themselves and many others life\'s at risk. For example, a distracted driver is, \"...23 times more likely to be in an accident,\" than a non-distracted driver. (National Highway Transportation Safety Administration). To continue, \"texting while driving is to blame for... 1,600,000 accidents per year, 330,000 injuries per year, and 11 teen deaths every day.\" (National Safety Council, Harvard Center for Risk Analysis Study, Institute for Highway Safety Fatality Facts). Therefore, it is proven that a distracted automobilist is a hazard for not only themselves, but also other motorists and pedestrians.

Furthermore, due to all the costly risks that come with texting and driving, such action has been made illegal in many states. Andrei Zakhareuski, from Driving Tests, proclaims that, \"Those who are caught will be issued a citation by a policeman who will most likely be quite perturbed at the driver\'s ignorance and poor decision after witnessing the devastating effects of texting and driving at accident sites...,\" and believes that, \" ... A text message that reads \"ok\" isn\'t worth a couple hundred dollar fine.\" Not to mention, those involved in a distracted driving related accident risk jail time, and most certainly, an increase in insurance rates. According to, 10 Pragmatic Reasons That Will Make You Stop Texting and Driving Today, \"If texting and driving is included in the police report for an accident or wreck for which you are held responsible, you\'ll notice an even more significant rate increase. In some cases, your policy might be dropped completely.\" Such a spike in cost or dropping of a policy would severely impact a driver. Hence, texting while driving is not worth the risk.

With the current trend of texting and driving, and all its risks included, drivers should not be allowed to operate cell phones while operating a vehicle. For, texting while driving takes a driver\'s attention off the road and endangers the lives of any passengers, other motorists, and pedestrians. Moreover, texting while driving increases a driver\'s chances of getting into an accident. As follows, once involved in a texting and driving related accident, either a driver\'s cost of a premium will skyrocket, or he or she will get dropped from their policy. To conclude, it is not safe nor wise for an automobilist to operate a cell phone while operating a vehicle.
output: Lead: The introduction sets the stage for the essay by addressing the common behavior of using cell phones while driving and the resulting debates. However, it could benefit from a more attention-grabbing device, such as a statistic or quotation, to enhance engagement.

Position: The main position is clear: drivers should not be allowed to operate cell phones while driving. This is explicitly stated in the introduction, providing a solid foundation for the essay.

Claim:Claim 1: Cell Phones as a Common Cause of Distracted Driving:
The claim is well-supported with a reference to the common causes of distracted driving. The inclusion of a statistic about the minimal time attention is taken away when texting and driving strengthens the argument.
Claim 2: Increased Risk of Accidents and Hazards:
The claim is supported with statistics highlighting the increased likelihood of accidents and the dangers of distracted driving. These statistics enhance the persuasiveness of the argument.
Claim 3: Legal Consequences and Risks:
The claim is well-supported with information about the legal consequences of texting and driving, including citations, jail time, and insurance rate increases. This provides a practical dimension to the argument.

Counterclaims and Rebuttals:The essay lacks explicit counterclaims and rebuttals. Addressing potential counterarguments would strengthen the overall argument by acknowledging opposing views.

Evidence:The essay provides strong evidence, including statistics and quotes, to support the claims. This enhances the credibility and persuasiveness of the argument.

Concluding Statement:The essay includes a concluding statement that summarizes the key points and reiterates the position that it is not safe or wise for a driver to operate a cell phone while driving.

input: Using a cell phone while operating a vehicle of any stature is a bad decision and should be illegal worldwide. Not only is using a cell phone while driving irresponsible, it\'s also dangerous to yourself, as well as others on the road. If one does choose to talk, text, or even try and use their cellular device while driving should be penalized to an extent and given a heavy warning. Though a warning, ticket, or even time served may be all it takes to prevent potentially fatal accidents on the road, these methods don\'t always work. Therefore we, as citizens, and as drivers, should be careful and wise with our decisions.

Reasons why driving and using your cell phone is so dangerous spans on and on. Firstly, one\'s not fully capable of providing one hundred percent of their attention to a single task such as driving while using their phone. Due to this, using your phone while driving only widens the window for a potential wreck, whether fatal or not. Studies show that using a cell phone and driving has become one of the top leading causes of car crashes in the past twenty years. Secondly, when one is distracted on the road, they put people in danger without even realizing it. There have been many instances where someone who is using their phone, ends up tailgating the vehicle ahead of them, with that vehicle potentially having an entire family in it. Many fatal crashes have been caused by this very action, injuring or even killing those involved in the wreck simply because someone wants to talk, text, or look at social media. So please, if you\'re driving, try and restrain from using your cell phone until you are parked in a secure location.

Not only is there a wide range of dangers when using your phone and driving, there\'s also a long list of punishments that follow close behind. One of the main punishments for driving and using your phone is a fine. These fines can range anywhere from $150 to $500 or more depending on how many offenses you have. With such pricey fines, you\'d think one would think twice before using their phone while operating a vehicle, but this isn\'t always the case. To counter this, those who repeat such actions can have their driver\'s license suspended for up to 90 days. Washington was the first to ban texting and driving state-wide with 38 other states following soon after. Some fines received in these states range from the minimum of $20 to a maximum of $10,000 and one year in prison. The average fine being around $150 to $375 in a handful of states. Insurance is another issue when it comes to using your phone while driving, with the coverage cost on your vehicle being affected. You see, the more of a risk you are on the road, the more you must pay on your insurance, so please drive safely.

Those who aren\'t fond of dangerous drivers should know how to avoid them and stay out of harm\'s way. One smart and helpful way to steer clear of those pesky drivers is to alert authorities. If you can, it\'s smart to try and obtain enough information about the driver and their vehicle such as a description of the driver or license plate. Calling 911 can be what saves you or someone else on the road from a potential accident. Another good way to prevent potential accidents is to travel when traffic is at its lowest. Driving in the early hours of the day can be a good time to drive, as well as work hours just before the lunch-rush. One would want to limit the amount of traffic on the road as much as possible in order to decrease the possibility of encountering dangerous drivers. Lastly, one simply needs to stay on high alert when driving. It seems like a no-brainer, yet many tend to not follow this basic rule of driving. Pay attention to details such as the speed you and those around you are going. Conditions on the road are also important, such as rain, snow, and ice. Remember that simply paying attention to the smaller details can prevent accidents on the road.
output: Lead: The introduction effectively grabs the reader\'s attention by stating a clear position and highlighting the dangers of using a cell phone while driving.

Position: The main position is clearly stated in the introduction: using a cell phone while driving should be illegal worldwide. This provides a strong foundation for the essay.

Claim:Claim 1: Lack of Attention and Increased Risk of Accidents:
The claim is supported with a valid reason and statistics highlighting the link between cell phone use and car crashes. This strengthens the argument.
Claim 2: Potential Harm to Others:
The claim is supported with examples of tailgating and fatal crashes caused by distracted drivers. This emphasizes the negative consequences of using a cell phone while driving.
Claim 3: Punishments and Consequences:
The claim is well-supported with information about fines, license suspensions, and insurance implications. This provides a practical aspect to the argument.
Claim 4: Avoiding Dangerous Drivers:
The claim offers practical advice on how to avoid dangerous drivers, such as alerting authorities and traveling during low-traffic hours. This adds value to the essay.

Counterclaims and Rebuttals:The essay lacks explicit counterclaims and rebuttals. Addressing potential counterarguments would strengthen the overall argument by acknowledging opposing views.

Evidence:The essay provides evidence, including statistics and examples, to support the claims. This enhances the credibility and persuasiveness of the argument.

Concluding Statement:The essay includes a concluding statement that summarizes the key points and reiterates the main position. It effectively emphasizes the importance of safe driving and avoiding cell phone use while operating a vehicle.

input: Whether or not you believe using your phone while operating a vehicle is as dangerous as it\'s portrayed to be, one cannot deny that it is a potential hazard. Many car crashes have occurred whilst using a phone and has become one of the leading causes of accidents on the road. Not only is it dangerous, but it is also illegal in most states and one could also be fined a hefty amount. It\'s simply a bad idea to text, talk, and overall use your phone while driving. Many tend to put responsible drivers in danger through these acts and fail to realize it until it\'s too late. Remember to drive responsibly, paying attention to those around you and how you drive. Your phone is not worth a life.       Imagien, you\'re going on a little vacation trip with your faimly or friends. But there\'s a program called the UNRRA

that you wanted to do. So you put it aside for next year becuase you wanted to hang out with your friends or faimly. Some people wanted to do things like programs or groups but couldn\'t becuase they have \"other things\" to do that aren\'t that really important. So this paper should make you think twice about going or signing up for the UNRRA program.

My first reason to join the UNRRA program is becuase you get to help other people in other countries that are in need for help or care. The UNRRA helpes people from Europe to China and give them stuff like food, water, and other things becuase of the war that happened in Europe which we call World War 2.

My second reason why you should join the UNRRA program is becuase that you get to see other countries or cities that aren\'t pausible to travel on foot, car, or train. You can get to see other counties like China, Greece, Crete, and even Panama Canal for a matter of fact.

My last reason to why you should join the UNRRA program is that there\'s fun activeities on the UNRRA ship to do. There\'s vollyball, boxing, table-tennis tornaments, fencing, baseball, whistleing, reading, and other sports or relaxing things to do before we go back to get more supplies for the people in Europe and people in other countries.
output:
""",
    **parameters
)
print(f"Response from Model: {response.text}")