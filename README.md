# Permaculture Plants:
##Database and look up engine
___

**Summary:** Written in Python 2.7. This Program is an open source project created for Permaculture Designers in temperate climates, specifically in the southern appalacian and midwestern region. However many of the plants may be practical in other temperate areas as well, such as in the pacific northwest and parts of Europe. It is intended to be a simple and easy quick reference that anyone can use. The database should be updated regularly to stay on top of new scientific information. Currently the only other easily accsessed index of this kind of information exists with-in books.

When doing a permaculture design it is important to consider as much information as possible about individual plants. Having all of this info easily accesible in one place is something that only exists (to my knowledge) in one book "Edible Food Forests: Volume 2." Creating this database will be useful for not only Permaculture designers but also gardeners, agriculturists, horticulturists and researchers.
___

##Information to Include:
1. Name

2. Plant Type

3. Uses(Functions)

4. Habitat Requirements

Currently we are using the appendices in "Edible Food Forest: Volume 2" for our information

**NOTE:** I am unaware of the copywright laws around taking documented information from books and placing them into computer databases. This will be figured out before releasing this program for use. If any one knows how the law applies here please let me know so that I can take the nessesary steps to make sure we are legal.

Any of the Information for each plant should return the plants name when searched.
**Example:**
Searching 'Nitrogen Fixer' would return the names of all plants that fix nitrogen. And searching a plant name should return All of its uses and habitat requirements

###Name:
1. Both common and scientific

###Plant Type:
1. Tree

2. Shrub

3. Herbacious Plant(perrenial/annual)

4. Ground Cover

###Uses:
1. Nitrogen Fixation

2. Dynamic Accumulation

3. Insect Attraction

4. Aromatic Confusion


###Habitat Requirements:
1. Zone

2. Sunlight

3. Soil

4. Water

5. Acidity
___
##The Code

This Program is written in Python 2.7, taking advantage of its strong database comprehension capabilities.

###Data Organization

**In Place:**

data by:

1. Function *in progress*. Structured as Dicionary of lists of tuples. Dictinary name = Function type: *eg. Nitrogen Fixer*, list name = kind of plant *Tree, Shrub, Ground cover, etc.* Tuples include two objects: Species of tree by scientific name first then by *most used* common name. First letter of first word capitalized for scientific, first letter of every word capitalized for common.
 
        Nitrogen = { 
            'Tree':[
                            ('Ainus cordata', 'Italian Alder'),
                            ('Ainus incana', 'Gray Alder'),
                            ('Maackia amurensis', 'Amur Maackia'),
                            ('Robinia pseudoacacia', 'Black Locus'),
                            ('Sophora japonica', 'Pagoda'),
                   ]

            'Shrub_large':[
                            ('Alnus rugosa', 'Speckeled Alder'),
                            ('Alnus serrulata', 'Smooth Alder'),
                            ('Amorsa fruticosa', 'False Indigo'),
                            ('Caragana arborascens', 'Siberian Pea Shrub'),
                            ('Caragana frutex', 'Russian Pea Shrub'),
                            ('Cercocarpus montanus', 'Mountain Mahogany'),
                            ('Colutea arborescens', 'Bladder Senna'),
                            ('Eleagnus commutata', 'Silverberry'),
                            ('Eleagnus multiflora', 'Goumi'),
                            ('Hippophae rhamnoides', 'Sea Buckthorn'),
                            ('Lespedeza bicolar', 'Bush Clover'),
                            ('Myrica cerifera', 'Wax Murtle'),
                            ('Myrica pensulvanica', 'Bay Berry'),
                            ('Prosopis glandulosa', 'Honeypod Mesquite'),
                            ('Robinia hispida', 'Bristly Locust'),
                            ('Robinia viscosa', 'Clammy Locust'),
                            ('Shepherdia canadensis', 'Buffalo Berry'),
                          ]
            };


2. ~~Habitat~~

3. ~~Name~~


###GUI

The Graphic User Interface will be written with Tkinter.
___

Any questions or suggestions can be sent to me at <rimannnhs@gmail.com>

