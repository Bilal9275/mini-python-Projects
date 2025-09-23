# 1- import random module
import random;

# 2- create a subjects list
subjects = ["A recent study", "Experts", "Scientists", "Researchers", "A new report" , "Health officials", "Government agencies", "Tech companies", "Environmentalists", "Economists"];

# 3- create a action list
actions = ["claims that", "suggests that", "proves that", "disputes that", "reveals that", "warns that", "announces that", "confirms that", "denies that", "predicts that"];

# 4- create a objects list
objects = ["eating chocolate", "drinking coffee", "exercising daily", "getting enough sleep", "meditating", "using social media", "working from home", "traveling frequently", "consuming fast food", "playing video games"];

# 5- create a places list
places = ["increases lifespan", "boosts brain power", "improves mood", "reduces stress", "enhances creativity", "causes weight gain", "leads to addiction", "improves productivity", "harms mental health", "supports immune system"];

# 6- start the headline generating loop
while True:
    # 7- randomly select one item from each list
    subject = random.choice(subjects);
    action = random.choice(actions);
    object_ = random.choice(objects);
    place = random.choice(places);
    
    # 8- construct the headline
    headline = f"{subject} {action} {object_} {place}.";
    
    # 9- print the generated headline
    print(headline);
    
    # 10- ask the user if they want to generate another headline
    again = input("Do you want to generate another headline? (yes/no): ");
    if again.lower() != 'yes':
        break;
     # 11- end the program
print("Thank you for using the news headline generator!");