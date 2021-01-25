from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO

#create genetic record from the genbank file
record = SeqIO.read("Genome.gb", "genbank")

#create diagram
gd_diagram = GenomeDiagram.Diagram("Tomato curly stunt virus")
#add new track for sequence features
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")

#create a set to add the sequence features that will be displayed
gd_feature_set = gd_track_for_features.new_set()

#look through all sequence features in the record (skip if not gene)
for feature in record.features:
    if feature.type != "gene":
        #Exclude this feature
        continue

    #5 different colors for features
    if len(gd_feature_set) % 5 == 0:
        color = colors.blue
    elif len(gd_feature_set) % 5 == 1:
        color = colors.green
    elif len(gd_feature_set) % 5 == 2:
        color = colors.red
    elif len(gd_feature_set) % 5 == 3:
        color = colors.yellow
    else:
        color = colors.lightblue

    #add the feature to the set and set label size/color/etc
    gd_feature_set.add_feature(feature, color=color, label_position="middle", label=True, label_size=15)


#draw the genome map
gd_diagram.draw(format="circular", circular=True, pagesize=(10*cm,10*cm),
                start=0, end=len(record), circle_core=0.7)
#output as PNG
gd_diagram.write("tomato_curly_stunt_virus_circular.png", "PNG")