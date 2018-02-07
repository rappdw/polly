import boto3
import os
import tempfile
import pyglet

if __name__ == '__main__':

    polly = boto3.client('polly')

    with tempfile.TemporaryDirectory() as tmp_dir:
        while True:
            input_text = input("Enter text to synthesize: ")
            if not input_text:
                break
            text = polly.synthesize_speech(Text=input_text, OutputFormat='ogg_vorbis', VoiceId='Brian')

            speach_file = os.path.join(tmp_dir, 'output.oggThi')
            with open(speach_file, 'wb') as f:
                f.write(text['AudioStream'].read())
                f.close()

            synthesized_speach = pyglet.media.load(speach_file)
            synthesized_speach.play()
            os.remove(speach_file)
