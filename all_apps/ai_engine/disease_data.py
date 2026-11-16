# Data for Cocoa
cocoa_class_names = [
    "black_pod_rot",
    "frosty_pod_rot",
    "healthy",
    "pod_borer",
    "witches_broom"
]

TREATMENTS_COCOA = {
    "black_pod_rot": (
        "Remove all infected and mummified pods from the trees and ground weekly, "
        "clear weeds and excess brush to improve air circulation, regulate heavy shade, "
        "and apply copper-based or systemic fungicides (such as copper oxychloride or Ridomil) "
        "starting at the onset of the rainy/monsoon season."
    ),
    "frosty_pod_rot": (
        "Harvest ripe pods regularly, prune infected and dead branches, perform weekly sanitary "
        "removal of diseased or sporulating pods (burying them at least 50 cm deep or destroying them), "
        "manage the canopy height to 10–12 feet to let sunlight in, and use integrated biological "
        "or low-toxicity chemical sprays."
    ),
    "healthy": (
        "Maintain routine crop monitoring at least once a week, perform annual post-harvest pruning, "
        "apply balanced soil nutrition, and keep drainage systems clear to prevent moisture buildup."
    ),
    "pod_borer": (
        "Inspect pods frequently for entry holes and bore dust, harvest pods as soon as they ripen "
        "to interrupt the pest cycle, remove and destroy infested pods, and apply targeted, "
        "recommended insecticides or biological controls only when economic threshold levels are exceeded."
    ),
    "witches_broom": (
        "Prune out all infected vegetative shoots and dry 'brooms' before the rainy season begins, "
        "collect and destroy all removed plant material away from the orchard, and plant resistant "
        "or hybrid cocoa varieties."
    )
}

IMPACT_COCOA = {
    "black_pod_rot": (
        "Causes severe yield loss by turning pods entirely black and rotting the internal beans, "
        "potentially destroying up to 30-50% of the entire annual harvest if left uncontrolled."
    ),
    "frosty_pod_rot": (
        "Drastically reduces usable pod production as the fungal pathogen deforms young pods, "
        "covering them in a thick, frost-like white spore layer that completely ruins the internal seed mass."
    ),
    "healthy": (
        "No negative impact; supports optimal vegetative growth, uniform pod development, "
        "and maximum premium bean yields per harvest cycle."
    ),
    "pod_borer": (
        "Severely damages cocoa pods and reduces quality by boring tunnels through the husk, "
        "disrupting internal nutrient distribution and causing beans to clump together flat, small, and unusable."
    ),
    "witches_broom": (
        "Reduces plant growth and productivity by forcing abnormal, erratic branching patterns "
        "that drain the tree's metabolic energy, leading to distorted flower cushions and starburst-shaped pods."
    )
}

SYMPTOMS_COCOA = {
    "black_pod_rot": "Small, dark brown or black necrotic lesions that rapidly expand to cover the entire pod surface, accompanied by a firm internal rot of the beans and a white fungal mycelium layer under humid conditions.",
    
    "frosty_pod_rot": "Early internal swelling and premature ripening of the pod, followed by a thick, compact, white-to-cream colored powdery fungal growth on the outer surface that later turns light brown as millions of spores mature.",
    
    "healthy": "Pods exhibit uniform, bright coloration characteristic of their variety (green, yellow, or red) with clean, unblemished surfaces, firm husks, healthy green leaves, and well-structured, normal branch development.",
    
    "pod_borer": "Tiny entrance and exit holes on the pod wall surface, early or uneven ripening of the husk, internal tunneling through the placenta, and clumped, damaged beans stuck together by larval frass (excrement).",
    
    "witches_broom": "Proliferation of tight, clustered, abnormal shoot growth forming thick 'brooms' from vegetative buds, accompanied by distorted flower cushions producing small, distorted, or star-shaped pods that harden and die early."
}


# Data for Potato & Tomato
potato_tomato_class_names = [
    "Potato_Early_blight",
    "Potato_Late_blight",
    "Potato_healthy",
    "Tomato_Early_blight",
    "Tomato_Late_blight",
    "Tomato_healthy"
]

TREATMENTS_POTATO_TOMATO = {
    "Potato_Early_blight": (
        "Apply protective fungicides (such as mancozeb or chlorothalonil) before disease onset, "
        "implement a strict 3-year crop rotation with non-solanaceous plants, optimize nitrogen fertilizer "
        "levels to reduce crop stress, and use drip irrigation to minimize leaf wetness."
    ),
    "Potato_Late_blight": (
        "Apply preventative systemic fungicides (such as metalaxyl or fluopicolide) during cool, humid weather, "
        "destroy all volunteer potatoes and cull piles, ensure proper hilling to protect buried tubers, "
        "and immediately destroy infected foliage (vine killing) at least two weeks before harvest."
    ),
    "Potato_healthy": (
        "Plant certified, disease-free seed tubers, maintain uniform soil moisture through scheduled "
        "irrigation, apply balanced N-P-K nutrition based on soil tests, and scout the field weekly "
        "for early signs of pests or nutrient deficiencies."
    ),
    "Tomato_Early_blight": (
        "Apply protective fungicides (such as chlorothalonil, mancozeb, or copper compounds) before disease onset, "
        "prune lower leaves up to 12 inches from the ground to prevent soil-splash inoculation, practice a 2-to-3-year "
        "crop rotation with non-solanaceous plants, and use drip irrigation to keep foliage completely dry."
        ),
    "Tomato_Late_blight": (
        "Apply preventative or systemic fungicides (such as mefenoxam, cymoxanil, or copper) immediately when cool, "
        "humid weather is forecast, destroy all volunteer tomato and potato plants, remove and destroy infected "
        "vines away from the field, and avoid overhead watering to prevent rapid zoospore spread."
        ),
    "Tomato_healthy": (
        "Plant certified disease-resistant seeds or transplants, maintain a consistent watering schedule using "
        "drip lines, apply balanced fertilizers rich in calcium to prevent blossom end rot, and implement "
        "routine staking and weeding to ensure optimal airflow throughout the canopy."
        )
}

IMPACT_POTATO_TOMATO = {
    "Potato_Early_blight": (
        "Causes premature defoliation that reduces the plant's photosynthetic capacity, "
        "leading to a significant reduction in tuber size, lower starch content, and "
        "surface lesions that diminish marketability and storage life."
    ),
    "Potato_Late_blight": (
        "Highly destructive disease that can completely destroy an entire field's foliage within days, "
        "causing total yield loss in the field and leading to rapid, foul-smelling bacterial soft rot "
        "that decimates stored tubers."
    ),
    "Potato_healthy": (
        "No negative impact; ensures maximum photosynthetic efficiency, optimal tuber bulking, "
        "high yield of premium-grade potatoes, and excellent long-term storage capability."
    ),
    "Tomato_Early_blight": (
        "Causes progressive defoliation starting from lower branches, exposing fruit to sunscald, "
        "reducing overall fruit size and yield quality, and causing dark, leathery lesions near "
        "the stem attachment that render the tomatoes unmarketable."
    ),
    "Tomato_Late_blight": (
        "Acts as a highly destructive pathogen capable of killing healthy plants within days, causing "
        "total crop failure in humid conditions, and producing large, rough, golden-brown greasy lesions "
        "on the fruit that lead to rapid secondary soft rots."
    ),
    "Tomato_healthy": (
        "No negative impact; ensures a robust vegetative growth phase, high rate of flower set, "
        "maximum yield of firm, uniform tomatoes, and standard post-harvest shelf life."
    )
}

SYMPTOMS_POTATO_TOMATO = {
    "Potato_Early_blight": "Dark brown to black circular spots with characteristic concentric rings ('target-board' appearance) on older lower leaves, surrounded by a chlorotic yellow halo, eventually causing leaves to dry up and drop.",
    "Potato_Late_blight": "Large, irregular, water-soaked dark green to purplish-black lesions on leaves and stems that rapidly expand, accompanied by a white, velvety fungal growth on the undersides of leaves during humid conditions.",
    "Potato_healthy": "Vibrant, uniformly green foliage with fully expanded leaves, strong erect stems, free of blemishes, spots, or chewing damage, yielding smooth, well-shaped tubers with intact skins.",
    "Tomato_Early_blight": "Small, dark brown to black spots with distinct concentric rings creating a 'target-board' pattern on older leaves, surrounded by yellow chlorotic halos, often accompanied by dark, sunken, leathery lesions at the stem end of the fruit.",
    "Tomato_Late_blight": "Large, irregular, water-soaked dark green to purplish-black lesions on leaves and stems that expand rapidly, accompanied by a delicate white, fuzzy fungal growth on the undersides of leaves during high humidity, and large, firm, greasy brown spots on the fruit.",
    "Tomato_healthy": "Vibrant, uniform green foliage free of spots or wilting, clean stems with strong upright growth, well-formed flower clusters, and smooth, unblemished fruit displaying even coloration according to ripeness stage."
    }


# Data for Cardamom
cardamom_class_names = [
    "Blight",
    "Healthy",
    "LeafSpot"
]

TREATMENTS_CARDAMOM = {
    "Blight": (
        "Collect and burn all severely infected leaves and dried pseudo-stems to eliminate inoculum sources. "
        "Improve field drainage, thin out excessive shade trees, and prune overcrowding tillers to maximize "
        "sunlight penetration and reduce humidity within the plant canopy. Apply a protective spray of 1% "
        "Bordeaux mixture or copper oxychloride (0.2%) at the onset of monsoon showers, repeating at 30-day "
        "intervals if high-moisture conditions persist."
    ),
    "Healthy": (
        "Maintain routine plantation monitoring at least once every two weeks. Implement balanced and "
        "split-dosage fertilizer applications based on soil health reports, manage the canopy to maintain "
        "50-60% filtered shade, and ensure proper irrigation management during dry summer months."
    ),
    "LeafSpot": (
        "Prune out and destroy the individual spotted leaves showing advanced necrosis during early stages. "
        "Clear low-lying weeds around the base of the cardamom clumps to lower ambient microclimate humidity. "
        "If the spotting spreads widely across the plantation, apply targeted systemic fungicides such as "
        "carbendazim (0.1%) or Mancozeb (0.2%) directly to the foliage to arrest spore propagation."
    )
}

IMPACT_CARDAMOM = {
    "Blight": (
        "Causes devastating economic yield loss by inducing extensive foliar necrosis and premature leaf drop, "
        "which drastically cripples the plant's photosynthetic capacity. Severe infections can dry up entire "
        "clumps, resulting in a 30-40% reduction in capsule production and poor quality, shriveled pods."
    ),
    "Healthy": (
        "No negative impact; supports optimal vegetative tiller production, robust panicle development, "
        "and maximum premium-grade green capsule yields per harvest cycle."
    ),
    "LeafSpot": (
        "Reduces effective leaf surface area and photosynthesis, which moderately impacts plant vigor and vitality. "
        "While less destructive than Blight, unchecked outbreaks lead to weaker pseudo-stems, fewer productive "
        "panicles, and a general decline in long-term crop yield over successive seasons."
    )
}

SYMPTOMS_CARDAMOM = {
    "Blight": "Large, irregular, water-soaked pale gray or brown lesions that rapidly spread across the leaf blade under humid conditions. The center of these lesions quickly dries up, becomes brittle, and tears away, often leaving the leaf scorched, shredded, or completely withered.",
    
    "Healthy": "Leaves display a vibrant, uniform dark green coloration without necrotic spotting or structural lesions. The leaves are firmly attached to sturdy, upright pseudo-stems with normal, well-structured tiller growth patterns.",
    
    "LeafSpot": "Numerous small, highly distinct, isolated round or oval spots distributed across the leaf surface. These spots typically feature a light gray or tan bleached center ringed by a sharp, dark brown or deep reddish-brown margin, giving them an eye-like appearance."
}

