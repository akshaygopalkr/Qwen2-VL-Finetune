import os
import json
import random

NO_VIOLATIONS = "There are no driving violations present in this video."
VIOLATION_FORMAT = "{i}. Violation {ca_vehicle_code}: {violation}, start time: {st}, end_time: {et}"
QUERY_MESSAGE = "Are there driving violations present in this video?"
DATA_PATH = '/home/ubuntu/akshay/data/driving_videos/jan_29_2025'


def format_data(sample):

    answer = ""
    if not sample["violations"]:
      answer = NO_VIOLATIONS
    else:
      answer = ""
      for j, v in enumerate(sample["violations"]):
        answer += VIOLATION_FORMAT.format(i=j+1, ca_vehicle_code=v["ca_vehicle_code"],
                                                 violation=v["violation"], st=v["start_time"], et=v["end_time"])
    vid_path = os.path.join(DATA_PATH, sample["name"])


    return {
       "id": sample["name"].split('.mp4')[0],
       "video": vid_path,
       "conversations": [
          {
             "from": "human",
             "value": "<video>\n" + QUERY_MESSAGE
          },
          {
             "from": "gpt",
             "value": answer
          }
       ]
    }


if __name__ == '__main__':

    # Load the video paths
    vid_path_dict = {f for f in os.listdir(DATA_PATH) if f.endswith('.MP4')}

    with open(os.path.join(DATA_PATH, 'jan_29_driving_labels.json'), 'r') as f:
        data = json.load(f)

    videos = data["videos"]
    random.seed(42)
    random.shuffle(videos)

    train_violations = set()
    test_violations = set()
    train_videos = videos[:int(len(videos)*0.8)]
    val_videos = videos[int(len(videos)*0.8):]


    for v in train_videos:
        if v["violations"]:

            violations = set([violation["ca_vehicle_code"] for violation in v["violations"]])
            train_violations = train_violations.union(violations)
    
    for v in val_videos:
        if v["violations"]:
            violations = set([violation["ca_vehicle_code"] for violation in v["violations"]])
            test_violations = test_violations.union(violations)

    print("Train violations: ", train_violations)
    print()
    print("Test violations: ", test_violations)
    print()

    # Find test violations not in train violations
    print("Test violations not in train violations: ", test_violations - train_violations)
    train_dataset = [format_data(v) for v in train_videos]
    val_dataset = [format_data(v) for v in val_videos]

    with open(os.path.join(DATA_PATH, 'train.json'), 'w') as f:
        json.dump(train_dataset, f, indent=4)
    with open(os.path.join(DATA_PATH, 'val.json'), 'w') as f:
        json.dump(val_dataset, f, indent=4)

