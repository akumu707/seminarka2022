import json
import os

def parse_lines(lines):
    episode = []
    for j, line in enumerate(lines):
        if line[0] == "\t":
            pass
        else:
            for i, char in enumerate(line):
                if char == ":":
                    if len(line) == i+1:
                        new_lines = []
                        for k in range(len(lines)):
                            if lines[j+k][0] == "\t":
                                new_lines.append(lines[j+k][1:])
                            if j+k+1 == len(lines):
                                break
                        episode.append({line[:i]: parse_lines(new_lines)})
                    else:
                        episode.append({line[:i]: line[i + 2:]})
    return episode


with open(os.path.join("resources", "data", "try.json"), "w", encoding="utf-8") as w_file:
    with open(os.path.join("try.txt"), "r", encoding="utf-8") as r_file:
        """
        for line in r_file:
            if number_of_tabs == 0:
                for i, char in enumerate(line):
                    if char == ":":
                        if line[i+1] == "\n":
                            number_of_tabs += 1
                            episode.append({line[:i]: []})
                        else:
                            episode.append({line[:i]: line[i+2:]})
            else:
                if line[number_of_tabs-1] == "  ":"""
        lines = []
        for line in r_file:
            lines.append(line[:-1])
        episode = parse_lines(lines)
        json.dump(episode, w_file, ensure_ascii=False, indent=4)

