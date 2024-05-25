import openai
import re

# 请将"your_api_key_here"替换为你的OpenAI API密钥
openai.api_key = "your_api_key_here"

def generate_lyrics(prompt, style):
    styles = {
        "pop": {"max_tokens": 1024, "temperature": 0.5, "stop": ["\n\n"]},
        "rock": {"max_tokens": 2048, "temperature": 0.7, "stop": ["\n\n", "Verse:"]},
        "country": {"max_tokens": 512, "temperature": 0.3, "stop": ["\n\n", "Chorus:"]},
        "jazz": {"max_tokens": 1024, "temperature": 0.6, "stop": ["\n\n"]},
        "classical": {"max_tokens": 1024, "temperature": 0.4, "stop": ["\n\n"]}
    }

    if style not in styles:
        raise ValueError("Invalid style. Please choose from 'pop', 'rock', 'country', 'jazz', 'classical'.")

    params = styles[style]

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=params["max_tokens"],
        n=1,
        stop=params["stop"],
        temperature=params["temperature"]
    )

    lyrics = response.choices[0].text
    lyrics = re.sub('[^0-9a-zA-Z\u4e00-\u9fa5\n.,?! ]+', '', lyrics)
    lyrics = lyrics.strip()

    return lyrics

def generate_sheet_music(lyrics):
    # 这里使用简化的方式生成歌词对应的简谱
    # 实际上可以通过音乐理论来进行更复杂的生成
    sheet_music = ""
    notes = ["C", "D", "E", "F", "G", "A", "B"]
    for line in lyrics.split('\n'):
        sheet_music += ' '.join(notes[i % len(notes)] for i, _ in enumerate(line.split())) + "\n"
    return sheet_music

def main():
    print("欢迎使用歌词生成器！")
    print("请按照提示输入歌曲标题和曲风，我们将为您生成歌词和简谱。")
    
    song_title = input("请输入歌曲标题：")
    print("请输入曲风（可选项：'pop', 'rock', 'country', 'jazz', 'classical'）：")
    song_style = input("曲风：")
    
    song_prompt = f"生成一首名为'{song_title}'的{song_style}歌曲，歌词如下：\n\n"
    
    try:
        song_lyrics = generate_lyrics(song_prompt, song_style)
        print(f"\n生成的'{song_title}'的{song_style}歌曲的歌词：\n\n{song_lyrics}")
        
        song_sheet_music = generate_sheet_music(song_lyrics)
        print(f"\n生成的'{song_title}'的简谱：\n\n{song_sheet_music}")
        
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"生成过程中出现错误：{e}")

if __name__ == "__main__":
    main()
