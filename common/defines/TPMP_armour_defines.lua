NDefines.NMilitary.LAND_COMBAT_STR_ARMOR_ON_SOFT_DICE_SIZE = 2	-- extra damage dice if our armor outclasses enemy
NDefines.NMilitary.LAND_COMBAT_ORG_ARMOR_ON_SOFT_DICE_SIZE = 5	-- extra damage dice if our armor outclasses enemy

NDefines.NMilitary.PIERCING_THRESHOLDS = {			-- Our piercing / their armor must be this value to deal damage fraction equal to the index in the array below [higher number = higher penetration]. If armor is 0, 1.00 will be returned.
		1.00,
		0.95,
		0.90,
		0.85,
		0.80,
		0.75,
		0.70,
		0.65,
		0.60,
		0.55,
		0.50,
		0.45,
		0.40,
		0.35,
		0.30,
		0.25,
		0.20,
		0.15,
		0.10,
		0.05,
		0.00						--there isn't much point setting this higher than 0
	}
NDefines.NMilitary.PIERCING_THRESHOLD_DAMAGE_VALUES = {		-- 0 armor will always receive maximum damage (so add overmatching at your own peril). the system expects at least 2 values, with no upper limit.
		1.00,
		0.97,
		0.95,
		0.92,
		0.89,
		0.87,
		0.84,
		0.81,
		0.77,
		0.74,
		0.71,
		0.67,
		0.63,
		0.59,
		0.55,
		0.50,
		0.45,
		0.39,
		0.32,
		0.22,
		0.00
	}

NDefines.NMilitary.ARMOR_VS_AVERAGE = 0.2			-- how to weight in highest armor & pen vs the division average
NDefines.NMilitary.PEN_VS_AVERAGE = 0.1
