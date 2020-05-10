from Image_Warping import image_warping

CARDS_PATH = "../Resources/cards.jpg"
POTTER_PATH = "../Resources/Harry_potter.jpg"
NEWS_PAPER_PATH = "../Resources/newspaper.jpeg"


def main():
    # image_warping.warp_image(FROM_POINT_LIST_POTTER, POTTER_PATH)
    image_warping.get_corners_by_clicks(POTTER_PATH)


if __name__ == '__main__':
    main()



