import json
import os


def parse_json_file(data_dir, json_dir):
    with open(json_dir, 'r') as j_f:
        json_obj = json.load(j_f)
    for file in json_obj["_via_img_metadata"].values():
        file_name = file["filename"].split('.')[0]
        with open(os.path.join(data_dir, file_name+".txt"), "w+") as f:
            for region in file["regions"]:
                coordinates = ",".join(["{},{}".format(x,y) for x,y in zip(region["shape_attributes"]["all_points_x"],
                                                               region["shape_attributes"]["all_points_y"])])
                f.write(coordinates + ',' + list(region["region_attributes"].values())[0] +  "\n")


if __name__ == '__main__':
    parse_json_file("data", "data/via_project_2Jan2021_20h30m.json")