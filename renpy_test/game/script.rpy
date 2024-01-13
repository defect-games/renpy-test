# The script of the game goes in this file.

# add splashscreen
label splashscreen:
    scene black
    with Pause(1)
    play music "audio/crime_test.mp3" fadein 1.0

    show text "Defect Games Presents..." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    

    return


# The game starts here.

label start:

    jump ch1Scene1GreatFarm

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    # e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
