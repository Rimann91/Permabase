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



for kind in Nitrogen:
    for specie in  Nitrogen[kind]:
        print specie
