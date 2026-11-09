Figure Requirements

Draw concentric circles representing the boundaries of five equal-length segments of toilet paper.

Each segment should contain 20% of the total paper. The innermost band should be the thickest, and the outermost should be the thinnest.

Draw the cardboard core with a radius of 1. The outside of a new roll should have a radius of 3 by default.

Calculate the boundaries by dividing the remaining fraction evenly from 0 to 1, then using my product_visible() function to convert each fraction into a radius. Do not use equal radial spacing.

Draw six boundary circles for five paper segments, including the cardboard boundary and the outer edge.

Use navy lines with a linewidth of 2 so the circles are easy to see.

Use an 8-by-6-inch figure and equal scaling on both axes so the circles look round instead of stretched.

Label the horizontal and vertical axes in units of cardboard core radii.

Include the title "Squares to Spare: 5 Equal Paper Segments" when n = 5. The title should automatically change for other segment counts.

The function should also work for n = 3 and n = 9.

Save the figures as roll_paradox_5.png, roll_paradox_3.png, and roll_paradox_9.png, depending on the number of segments.

Expected Result

I expect the figure to show five bands around a cardboard core. Even though each band represents the same amount of paper, the bands should get thinner toward the outside. This should demonstrate why judging the amount of toilet paper remaining by the visible radius can be misleading.