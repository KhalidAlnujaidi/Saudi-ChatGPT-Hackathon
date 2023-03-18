![saudi](https://user-images.githubusercontent.com/93127443/226091650-606a897a-c964-4d4d-a32e-b728dcd58585.png)


# Intelligent Avatar


The idea is a super intelegent avatar that can fleuntly conversate with users.

The avatar is for the most part powered by OpenAI's technology. It uses whisper and ChatGPT models to communicate.
The text output of ChatGPT is then fed into a Text-to-Visual-Speech, that produces both pychiacal animation and a voice.

Short 2:30 minutes live working demo of a Voice-to-voice convo with the avatar: https://youtu.be/a2JKVeLiWJk it was asked to act as a tour guide and talk a bit about Saudi Arabia and then NEOM.

As a starting point and proof of concept, the avatars presented in the project are a product of movio.la studio, which provides an API as well as traditional transactional means. However, the goal of the project is to have a fixed set of in-house developed avatars. This approach will increase the quality of animation, while also reducing costs and improving computational efficiency and latency of responses. To achieve this, we need a small team of developers and proper resources. 

With these in place, we estimate that the project could be completed by the end of the summer.


#### To try out the app
- ffmpeg must be installed in the system <br>
- ```git clone https://github.com/KhalidAlnujaidi/Saudi-ChatGPT-Hackathon.git
cd Saudi-ChatGPT-Hackathon.git 
pip install -r requirements.txt ```



- ffmpeg: `sudo apt-get install ffmpeg`
- Install necessary packages using `pip install -r requirements.txt`. Alternatively, instructions for using a docker image is provided [here](https://gist.github.com/xenogenesi/e62d3d13dadbc164124c830e9c453668). Have a look at [this comment](https://github.com/Rudrabha/Wav2Lip/issues/131#issuecomment-725478562) and comment on [the gist](https://gist.github.com/xenogenesi/e62d3d13dadbc164124c830e9c453668) if you encounter any issues. 
- Face detection [pre-trained model](https://www.adrianbulat.com/downloads/python-fan/s3fd-619a316812.pth) should be downloaded to `face_detection/detection/sfd/s3fd.pth`. Alternative [link](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/prajwal_k_research_iiit_ac_in/EZsy6qWuivtDnANIG73iHjIBjMSoojcIV0NULXV-yiuiIg?e=qTasa8) if the above does not work.
