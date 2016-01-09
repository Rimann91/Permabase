for kind in Nitrogen:
    for specie in  Nitrogen[kind]:
        print specie

choice = str(raw_input('what kind of plant?  '))

def whatkind(choice):
    if choice == 'trees':
        for kind in Nitrogen:
            for specie in Nitrogen[kind]:
                print "scientific: " + str(specie[0])
                print "common: " + str(specie[1])
                print
    else:
        return false

whatkind(choice)




Nitrogen = {
            'Tree':[
                            ('Ainus cordata', 'Italian Alder'),
                            ('Ainus incana', 'Gray Alder'),
                            ('Maackia amurensis', 'Amur Maackia'),
                            ('Robinia pseudoacacia', 'Black Locus'),
                            ('Sophora japonica', 'Pagoda'),
                   ],

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
                          ],

            'Shrub_medium':[
                            ('Acacia angustissima', 'Prarie Acacia'),
                            ('Acacia angustissima hirta', "Dwarf Prarie Acacia"),
                            ('Amorpha canescens', 'Leadplant'),
                            ('Amorpha nana', 'Fragrant Indigobush'),
                            ('Caragana pygmaea', 'Pygmy Pea Shrub'),
                            ('Ceanothus americanus', 'New Jersey Tea'),
                            ('Comptonia peregrina', 'Sweet Fern'),
                            ('Genista Pilosa', 'Silky Leaf Woodwaxen'),
                            ('Genista tinctoria', "Dyer's Greenwood"),
                            ('Hippophae Rhamnoides cv.', "Sea Buckthorn 'Dorana Dwarf'"),
                            ('Indigofera Decora', 'Chinese Indigo'),
                            ('Myrica gale', 'Sweet Gale'),
            
            'shrub_small':[
                            ('Ceanothus prostratus',  'Mahala Mat')
                            ('Cytisus decumbens',  'Prostrate Broom')
                            ('Dryas octopetala',  'Mountain Avens')
                            ('Genista pilosa procumbens',  'Prostrate Woodwaxen')
                            ('Genista Sagittalis',  'Arrow Broom')
                    ],

             'vines': [
                            ('Amphicarpaea bracteata',  'Hog Pea'),
                            ('Apios americana',  'Ground Nut'),
                            ('Apios fortunei',  'Fortunes Groundnut'),
                            ('Apios priceana',  'Prices Groundnut'),
                            ('Clitoria mariana',  'Butterfly Pea'),
                            ('Lathyrus japonicus maritima',  'Beach Pea'),
                            ('Lathyrus latifolius',  'Everlasting Pea'),
                            ('Lathyrus linifolius montanus',  'Bitter Vetch'),
                            ('Lathyrus tuberosis',  'Earthnut Pea'),
                            ('Phaseolus polystachios',  'Wild Bean'),
                            ('Strophostyles umbelleta',  'Wild Bean'),
                            ('Vivia americana',  'American Vetch'),
                            ('Vicia Carolintana',  'Wood Vetch'),
                            ('Vicia cracca',  'Tufted Vetch'),
                            ('Wisteria floribunda',  'Japanese Wysteria'),
                            ('Wisteria frutescens',  'American Wisteria'),
                            ('Wisteria mascrostachya',  'Kentucky Wisteria'),
                    ],

             'Med_lrg_herbs': [
                            ('Astragalus canadensis',  'Canada Milkvetch'),
                            ('Astragalus membranaceous',  'Huang-qi'),
                            ('Babtisia australis',  'Blue Wild Indigo'),
                            ('Babtisia tinctoria',  'Yellow Wild Indigo'),
                            ('Desmodium canadens',  'Showy Tick Trefoil'),
                            ('Desmodium glitinosum',  'Pointed-leaf Tick Trefoil'),
                            ('Glycyrrhiza glabra',  'Licorice'),
                            ('Glycyrrhiza lepidota',  'American Licorice'),
                            ('Glycyrrhiza uralensis',  'Chinese Licorice'),
                            ('Hedysarum boreale',  'Sweet Vetch'),
                            ('Lespedeza capitata',  'Round-headed Bush Clover'),
                            ('Lupinus perennis',  'Wild Lupine'),
                            ('Lupinus hybrids',  'Hybrid Lupines'),
                            ('Medicago sativa',  'Alfalfa'),
                            ('Thermopsis villosa',  'Carolina Bush Pea'),
                            ('Trifollium pratense',  'Red Clover'),
                    ],

             'herbs_small': [
                            ('Astragalus crassicarpus',  'Ground Milk Vetch'),
                            ('Astragalus glycyphyllos',  'Milk Vetch'),
                            ('Lotus cornicultasus cv.',  'Prostrate Birds-foot Trefoil'),
                            ('Psoralea esculenta',  'Prarie Turnip'),
                            ('Stylosanthes biflora',  'Prncil Flower'),
                            ('Rifolium repens',  'White Clover'),
                    ],

            }

Dynamic = {
             'all': [
                            ('Acer saccharum',  'Sugar Maple', 'K', 'Ca'),
                            ('Acer spp.',  'Maples', 'k'),
                            ('Achillea millefolium',  'Yarrow', 'K', 'P', 'Cu'),
                            ('Allium Schoenoprasum',  'Chives', 'K', 'Ca'),
                            ('Betula lenta',  'Black Birch', 'K', 'P', 'Ca'),
                            ('Betula spp.',  'Birches', 'P'),
                            ('Brassica spp.',  'Perrenial Brassicas', 'P', 'S'),
                            ('Carya ovata',  'Shagbark Hickory', 'K', 'P', 'Ca'),
                            ('Carya spp.',  'Hickory and Pecan', 'K', 'Ca'),
                            ('Chamaemelum nobile',  'German Chamomile', 'K', 'P', 'Ca'),
                            ('Cichorium intybus',  'Chicory', 'K', 'Ca'),
                            ('Cornus florida',  'Flowering Dogwood', 'K', 'P', 'Ca'),
                            ('Equisetum spp.',  'Horsetails', 'Ca', 'Co', 'Fe', 'Mg'),
                            ('Fagus',  'Beeches', 'K'),
                            ('Fagus sylvatica',  'European Beech', 'K', 'Ca'),
                            ('Fragaria spp.',  'Strawberry', 'Fe'),
                            ('Gaultheria procumbens',  'Wintergreen', 'Mg'),
                            ('Glycyrrhiza spp.',  'Licorices', 'P', 'N2'),
                            ('Juglans spp.',  'Walnuts', 'K', 'P'),
                            ('Juglans nigra',  'Black Walnut', 'K', 'P', 'Ca'),
                            ('Lupinus spp.',  'Lupines', 'P', 'N2'),
                            ('Malus spp.',  'Apples', 'K'),
                            ('Medicago sativa',  'Alfalfa' ,'Fe', 'N2'),
                            ('Mentha x piperita',  'Peppermint', 'K', 'Mg'),
                            ('Melissa officinalis',  'Lemon Balm', 'P'),
                            ('Nasturtium officinale',  'Watercress', 'K', 'P', 'Ca', 'S', 'Fe', 'Mg', 'Na'),
                            ('Potentilla anserina',  'Silverweed', 'K', 'Ca', 'Cu'),
                            ('Quercus alba',  'White Oak', 'P'),
                            ('Robinia psuedoacacia',  'Black Locust', 'K', 'Ca', 'N2'),
                            ('Rumex spp.',  'Sorrels and Docks', 'K', 'P', 'Ca', 'Fe', 'Na'),
                            ('Sanguisorba minor',  'Salad Burnet', 'Fe'),
                            ('Satureja spp.',  'Savory', 'P'),
                            ('Stellaria media',  'Chickweed', 'K', 'P'),
                            ('Symphytum spp.',  'Comfreys', 'K', 'P', 'Ca', 'Cu', 'Fe', 'Mg'),
                            ('Taraxacum officinale',  'Dandelion', 'K', 'P', 'Ca', 'Cu', 'Fe'),
                            ('Tilia americana',  'Basswood', 'P', 'Ca', 'Mg'),
                            ('Tilia spp.',  'Linden', 'P', 'Ca'),
                            ('Trifolium spp.',  'Clovers', 'P'),
                            ('Urtica dioica',  'Stinging Nettle', 'K', 'Ca', 'S', 'Cu', 'Fe', 'Na'),
                            ('Vicia spp.',  'vetches', 'K', 'P', 'N2'),
                            ('Viola spp.',  'Violets', 'P'),
                    ],

             'potassium': [
                            ('Acer saccharum',  'Sugar Maple'),
                            ('Acer spp.',  'Maples'),
                            ('Achillea millefolium',  'Yarrow'),
                            ('Allium schoenoprasum',  'Chives'),
                            ('Butela lenta',  'Black Birch'),
                            ('Carya spp.',  'Hickory and Pecan'),
                            ('Chamaemelum nobile',  'German Chamomile'),
                            ('Cichorium intybus',  'Chicory'),
                            ('Cornus florida',  'Flowering Dogwood'),
                            ('Fagus spp.',  'Beeches'),
                            ('Juglans spp.',  'Walnuts'),
                            ('Malus spp.',  'Apples'),
                            ('Mentha x piperita',  'Peppermint'),
                            ('Nasturtium officinale',  'Watercress'),
                            ('Potentilla anserina',  'Silverweed'),
                            ('Robinia psuedoacacia',  'Black Locust'),
                            ('Rumex spp.',  'Dock and Sorrels'),
                            ('Stellaria media',  'Chickweed'),
                            ('Symphytum spp.',  'Comfreys'),
                            ('Taraxacum officinale',  'Dandelion'),
                            ('Urtica dioica',  'Stinging Nettle'),
                            ('Vicia spp.',  'Vetches'),
                    ],

             'Phosphorous': [
                            ('Achillea millefolium',  'Yarrow'),
                            ('Betula lenta',  'Black Birch'),
