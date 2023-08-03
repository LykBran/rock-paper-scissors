import jetson_inference
import jetson_utils
import argparse
import sys
import random

argv = (
    sys.argv
    if sys.argv == []
    else [
        "--input_blob=input_0",
        "--output_blob=output_0",
        "--model=resnet18.onnx",
        "--labels=labels.txt",
    ]
)
parser = argparse.ArgumentParser(
    description="Classify a live camera stream using an image recognition DNN.",
    formatter_class=argparse.RawTextHelpFormatter,
    epilog=jetson_inference.imageNet.Usage()
    + jetson_utils.videoSource.Usage()
    + jetson_utils.videoOutput.Usage()
    + jetson_utils.Log.Usage(),
)

parser.add_argument(
    "input", type=str, default="/dev/video0", nargs="?", help="URI of the input stream"
)
parser.add_argument(
    "--network",
    type=str,
    default="googlenet",
    help="pre-trained model to load (see below for options)",
)

try:
    args = parser.parse_known_args()[0]
except:
    print("")
    parser.print_help()
    sys.exit(0)

print(args.network)
net = jetson_inference.imageNet(args.network, argv=argv)
stream_in = jetson_utils.videoSource(args.input)

font = jetson_utils.cudaFont()

while True:
    print("Press [enter] to start a new game.")
    input()
    img = stream_in.Capture()
    class_id, confidence = net.Classify(img)
    class_desc = net.GetClassDesc(class_id)
    print(
        f"You probably chose {class_desc} (class #{class_id} with {confidence * 100}% confidence)."
    )
    computer_choice = random.randint(0, 2)
    print(f"Computer chose {net.GetClassDesc(computer_choice)}.")
    """
0 : paper
1 : rock
2 : scissors
    """
    result = (class_id - computer_choice) % 3
    if result == 0:
        msg = "Wow, It's a draw! Cool."
    elif result == 1:
        msg = "What a pity! You lose the game."
    else:
        msg = "Congratulations! You win the game."
    print(msg)
