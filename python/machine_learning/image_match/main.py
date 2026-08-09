import cv2 as cv
import check

# Note:
# - More than 3 pixel shift in the image should be rejected
# - Less than 5 pixels changed in the whole image should be accepted

# Uses images in folder 1
def test1():
    image1 = "images/1/image1.png"

    # Should pass - same image but different colour
    image2 = "images/1/image2a.png"  # 99
    image2a1 = "images/1/image2a1.png"  # --

    # Should pass
    image3 = "images/1/image2b1.png"  # 11 matches
    image4 = "images/1/image2b2.png"  # 9 matches
    image5 = "images/1/image2b3.png"  # 10 matches
    image6 = "images/1/image2c.png"  # 6 matches

    # Rejects
    image7 = "images/1/image3a.png"  # 4 matches
    image8 = "images/1/image3b.png"  # 2 matches

    # Rejects - Different
    image9 = "images/1/image4a.png"  # 0 matches
    image10 = "images/1/image4b.png"  # 7 matches
    image11 = "images/1/image4c.png"  # 4 matches

    # Rejects - Very Different
    image100 = "images/1/image100a.png"  # 0 matches
    image101 = "images/1/image100b.png"  # 0 matches
    image102 = "images/1/image100c.png"  # 2 matches

    check.check1(image1, image1)
    check.check1(image1, image2)
    check.check1(image1, image2a1)
    check.check1(image1, image3)
    check.check1(image1, image4)
    check.check1(image1, image5)
    check.check1(image1, image6)
    check.check1(image1, image7)
    check.check1(image1, image8)
    check.check1(image1, image9)
    check.check1(image1, image10)
    check.check1(image1, image11)
    check.check1(image1, image100)
    check.check1(image1, image101)
    check.check1(image1, image102)


# Uses images in folder 2
def test2():
    image1a = "images/2/le13-frame.png"  # - matches
    image1b = "images/2/le13-noframe.png"  # - matches
    image2a = "images/2/scrolldownbutton-enabled.png"  # - matches
    image2b = "images/2/scrolldownbutton-notenabled.png"  # - matches
    image3a = "images/2/scrollupbutton-notpressed.png"  # - matches
    image3b = "images/2/scrollupbutton-pressed.png"  # - matches
    image4a = "images/2/speedmeter-fullmode.png"  # - matches
    image4b = "images/2/speedmeter-ltmode.png"  # - matches
    image5a = "images/2/tt1a.png"  # - matches
    image5b = "images/2/tt1b.png"  # - matches

    check.check1(image1a, image1b)
    check.check1(image2a, image2b)
    check.check1(image3a, image3b)
    check.check1(image4a, image4b)
    check.check1(image5a, image5b)

def test3():
    image1 = "images/1/image1.png"
    image2a1 = "images/1/image2a1.png"  # --

    image5a = "images/2/tt1a.png"  # - matches
    image5b = "images/2/tt1b.png"  # - matches

    check.check1(image1, image2a1)
    check.check1(image5a, image5b)


# Main control
#test1()
#test2()
test3()

print("End")
