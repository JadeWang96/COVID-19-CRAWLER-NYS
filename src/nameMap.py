"""
@ProjectName: DXY-2019-nCov-Crawler
@FileName: countryTypeMap.py
@Author: Jiabao Lin
@Date: 2020/1/22
@Modifier: Jade Wang
@Data: 2020/3/20
"""

# Change the map data depends on your needs
# County name from https://www.ng3k.com/Misc/usc_n.html#ny
new_york_county_map = {
    'Albany': 'Albany County',
    'Allegany': 'Allegany County',
    'Bronx': 'Bronx County',
    'Broome': 'Broome County',
    'Cattaraugus': 'Cattaraugus County',
    'Cayuga': 'Cayuga County',
    'Chautauqua': 'Chautauqua County',
    'Chemung': 'Chemung County',
    'Chenango': 'Chenango County',
    'Clinton': 'Clinton County',
    'Columbia': 'Columbia County',
    'Cortland': 'Cortland County',
    'Delaware': 'Delaware County',
    'Dutchess': 'Dutchess County',
    'Erie': 'Erie County',
    'Essex': 'Essex County',
    'Franklin': 'Franklin County',
    'Fulton': 'Fulton County',
    'Genesee': 'Genesee County',
    'Greene': 'Greene County',
    'Hamilton': 'Hamilton County',
    'Herkimer': 'Herkimer County',
    'Jefferson': 'Jefferson County',
    'Kings': 'Kings County',
    'Lewis': 'Lewis County',
    'Livingston': 'Livingston County',
    'Madison': 'Madison County',
    'Monroe': 'Monroe County',
    'Montgomery': 'Montgomery County',
    'Nassau': 'Nassau County',
    'New York City': 'New York County',
    'Niagara': 'Niagara County',
    'Oneida': 'Oneida County',
    'Onondaga': 'Onondaga County',
    'Ontario': 'Ontario County',
    'Orange': 'Orange County',
    'Orleans': 'Orleans County',
    'Oswego': 'Oswego County',
    'Otsego': 'Otsego County',
    'Putnam': 'Putnam County',
    'Queens': 'Queens County',
    'Rensselaer': 'Rensselaer County',
    'Richmond': 'Richmond County',
    'Rockland': 'Rockland County',
    'Saratoga': 'Saratoga County',
    'Schenectady': 'Schenectady County',
    'Schoharie': 'Schoharie County',
    'Schuyler': 'Schuyler County',
    'Seneca': 'Seneca County',
    'St.Lawrence': 'St.Lawrence County',
    'Steuben': 'Steuben County',
    'Suffolk': 'Suffolk County',
    'Sullivan': 'Sullivan County',
    'Tioga': 'Tioga County',
    'Tompkins': 'Tompkins County',
    'Ulster': 'Ulster County',
    'Warren': 'Warren County',
    'Washington': 'Washington County',
    'Wayne': 'Wayne County',
    'Westchester': 'Westchester County',
    'Wyoming': 'Wyoming County',
    'Yates': 'Yates County'
}

state_name_map = {
    'Alabama': {
        'Abbreviation': 'AL',
        # 'Counties': {
        #
        # }
    },
    'Alaska': {
        'Abbreviation': 'AK',
        # 'Counties': {
        #
        # }
    },
    'Arizona': {
        'Abbreviation': 'AZ',
        # 'Counties': {
        #
        # }
    },
    'Arkansas': {
        'Abbreviation': 'AR',
        # 'Counties': {
        #
        # }
    },
    'California': {
        'Abbreviation': 'CA',
        # 'Counties': {
        #
        # }
    },
    'Colorado': {
        'Abbreviation': 'CO',
        # 'Counties': {
        #
        # }
    },
    'Connecticut': {
        'Abbreviation': 'CT',
        # 'Counties': {
        #
        # }
    },
    'Delaware': {
        'Abbreviation': 'DE',
        # 'Counties': {
        #
        # }
    },
    'Florida': {
        'Abbreviation': 'FL',
        # 'Counties': {
        #
        # }
    },
    'Georgia': {
        'Abbreviation': 'GA',
        # 'Counties': {
        #
        # }
    },
    'Hawaii': {
        'Abbreviation': 'HI',
        # 'Counties': {
        #
        # }
    },
    'Idaho': {
        'Abbreviation': 'ID',
        # 'Counties': {
        #
        # }
    },
    'Illinois': {
        'Abbreviation': 'IL',
        # 'Counties': {
        #
        # }
    },
    'Indiana': {
        'Abbreviation': 'IN',
        # 'Counties': {
        #
        # }
    },
    'Iowa': {
        'Abbreviation': 'IA',
        # 'Counties': {
        #
        # }
    },
    'Kansas': {
        'Abbreviation': 'KS',
        # 'Counties': {
        #
        # }
    },
    'Kentucky': {
        'Abbreviation': 'KY',
        # 'Counties': {
        #
        # }
    },
    'Louisiana': {
        'Abbreviation': 'LA',
        # 'Counties': {
        #
        # }
    },
    'Maine': {
        'Abbreviation': 'ME',
        # 'Counties': {
        #
        # }
    },
    'Maryland': {
        'Abbreviation': 'MD',
        # 'Counties': {
        #
        # }
    },
    'Massachusetts': {
        'Abbreviation': 'MA',
        # 'Counties': {
        #
        # }
    },
    'Michigan': {
        'Abbreviation': 'MI',
        # 'Counties': {
        #
        # }
    },
    'Minnesota': {
        'Abbreviation': 'MN',
        # 'Counties': {
        #
        # }
    },
    'Mississippi': {
        'Abbreviation': 'MS',
        # 'Counties': {
        #
        # }
    },
    'Missouri': {
        'Abbreviation': 'MO',
        # 'Counties': {
        #
        # }
    },
    'Montana': {
        'Abbreviation': 'MT',
        # 'Counties': {
        #
        # }
    },
    'Nebraska': {
        'Abbreviation': 'NE',
        # 'Counties': {
        #
        # }
    },
    'Nevada': {
        'Abbreviation': 'NV',
        # 'Counties': {
        #
        # }
    },
    'New Hampshire': {
        'Abbreviation': 'NH',
        # 'Counties': {
        #
        # }
    },
    'New Jersey': {
        'Abbreviation': 'NJ',
        # 'Counties': {
        #
        # }
    },
    'New Mexico': {
        'Abbreviation': 'NM',
        # 'Counties': {
        #
        # }
    },
    'New York': {
        'Abbreviation': 'NY',
        # 'Counties': {
        #
        # }
    },
    'North Carolina': {
        'Abbreviation': 'NC',
        # 'Counties': {
        #
        # }
    },
    'North Dakota': {
        'Abbreviation': 'ND',
        # 'Counties': {
        #
        # }
    },
    'Ohio': {
        'Abbreviation': 'OH',
        # 'Counties': {
        #
        # }
    },
    'Oklahoma': {
        'Abbreviation': 'OK',
        # 'Counties': {
        #
        # }
    },
    'Oregon': {
        'Abbreviation': 'OR',
        # 'Counties': {
        #
        # }
    },
    'Pennsylvania': {
        'Abbreviation': 'PA',
        # 'Counties': {
        #
        # }
    },
    'Rhode Island': {
        'Abbreviation': 'RI',
        # 'Counties': {
        #
        # }
    },
    'South Carolina': {
        'Abbreviation': 'SC',
        # 'Counties': {
        #
        # }
    },
    'South Dakota': {
        'Abbreviation': 'SD',
        # 'Counties': {
        #
        # }
    },
    'Tennessee': {
        'Abbreviation': 'TN',
        # 'Counties': {
        #
        # }
    },
    'Texas': {
        'Abbreviation': 'TX',
        # 'Counties': {
        #
        # }
    },
    'Utah': {
        'Abbreviation': 'UT',
        # 'Counties': {
        #
        # }
    },
    'Vermont': {
        'Abbreviation': 'VT',
        # 'Counties': {
        #
        # }
    },
    'Virginia': {
        'Abbreviation': 'VA',
        # 'Counties': {
        #
        # }
    },
    'Washington': {
        'Abbreviation': 'WA',
        # 'Counties': {
        #
        # }
    },
    'West Virginia': {
        'Abbreviation': 'WV',
        # 'Counties': {
        #
        # }
    },
    'Wisconsin': {
        'Abbreviation': 'WI',
        # 'Counties': {
        #
        # }
    },
    'Wyoming': {
        'Abbreviation': 'WY',
        # 'Counties': {
        #
        # }
    },
    'Washington, D.C.': {
        'Abbreviation': 'DC',
        # 'Counties': {
        #
        # }
    },
    'US Virgin Islands': {
        'Abbreviation': 'None',
        # 'Counties': {
        #
        # }
    },
    'Diamond Princess': {
        'Abbreviation': 'None',
        # 'Counties': {
        #
        # }
    },
    'Grand Princess': {
        'Abbreviation': 'None',
        # 'Counties': {
        #
        # }
    },
    'Puerto Rico': {
        'Abbreviation': 'PR',
        # 'Counties': {
        #
        # }
    },
    'Wuhan Evacuee': {
        'Abbreviation': 'None',
        # 'Counties': {
        #
        # }
    },
    'Guam': {
        'Abbreviation': 'None',
        # 'Counties': {
        #
        # }
    }

}
