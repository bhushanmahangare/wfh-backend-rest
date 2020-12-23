from enum import IntEnum, Enum


class UserType(IntEnum):
    SUPER_ADMIN = 1
    IT_ADMIN = 2
    MANAGER = 3
    SUBSCRIBER = 4

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class CustomerStatus(Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    SUSPENDED = "suspended"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Features(Enum):
    CONTENT_FILTER = "content_filter"
    CAPTIVE_PORTAL = "captive_portal"
    WIPS = "wips"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class Roles(Enum):
    HIDDEN = 1 
    READ_ONLY = 2
    EDIT = 3
    FULL_CONTROL = 4 

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class DateFormat(IntEnum):
    d_m_Y = 1
    m_d_Y = 2
    d_M_Y = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class LevelType(Enum):
    GROUP = "group"
    LOCATION = "location"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class TimeUnits(Enum):
    SECOND = 1
    MINUTE = 2
    HOUR = 3
    DAY = 4
    WEEK = 5

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


# AP Configurtions
class SecurityTypes(Enum):
    OPEN = 1
    WPA_2_PSK = 2
    WPA_2_PSK_801_1x = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class BroadcastingBand(Enum):
    RADIO_1 = 1
    RADIO_2 = 2
    RADIO_3 = 3
    ALL = 4

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class CipherType(Enum):
    TKIP = 1
    CCMP = 2
    TKIP_CCMP = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class FTProtocol(Enum):
    FT_OVER_DS = 1
    FT_OVER_AIR = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class ActionTypes(Enum):
    ALLOW = "allow"
    DENY = "deny"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class MultiwanMethods(Enum):
    LOAD_BALANCING = "loadbalancing"
    FAIL_OVER = "failover"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class LanPortModes(Enum):
    PRIVATE = "privatelan"
    HOTSPOT = "hotspot"
    DAISYCHAIN = "daisychain"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class SDWanType(Enum):
    WAN = "wan"
    VPN = "vpn"
    GRE = "gre"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class TrafficFlowTypes(Enum):
    L2 = "l2"
    L3 = "l3"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class DataFormat(Enum):
    CSV = "csv"
    JSON = "json"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class DataUploadUnit(Enum):
    SECOND = 1
    MINUTE = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class CountryCodes(Enum):
    AF = "Afghanistan"
    AL = "Albania"
    DZ = "Algeria"
    AS = "American Samoa"
    AD = "Andorra"
    AO = "Angola"
    AI = "Anguilla"
    AQ = "Antarctica"
    AR = "Argentina"
    AM = "Armenia"
    AW = "Aruba"
    AU = "Australia"
    AT = "Austria"
    AZ = "Azerbaijan"
    BS = "Bahamas"
    BH = "Bahrain"
    BD = "Bangladesh"
    BB = "Barbados"
    BY = "Belarus"
    BE = "Belgium"
    BZ = "Belize"
    BJ = "Benin"
    BM = "Bermuda"
    BT = "Bhutan"
    BO = "Bolivia"
    BA = "Bosnia and Herzegowina"
    BW = "Botswana"
    BV = "Bouvet Island"
    BR = "Brazil"
    IO = "British Indian Ocean Territory"
    BN = "Brunei Darussalam"
    BG = "Bulgaria"
    BF = "Burkina Faso"
    BI = "Burundi"
    KH = "Cambodia"
    CM = "Cameroon"
    CA = "Canada"
    CV = "Cape Verde"
    KY = "Cayman Islands"
    CF = "Central African Republic"
    TD = "Chad"
    CL = "Chile"
    CN = "China"
    CX = "Christmas Island"
    CC = "Cocos (Keeling) Islands"
    CO = "Colombia"
    KM = "Comoros"
    CG = "Congo"
    CD = "Congo the Democratic Republic of the"
    CK = "Cook Islands"
    CR = "Costa Rica"
    CI = "Cote d'Ivoire"
    HR = "Croatia (Hrvatska)"
    CU = "Cuba"
    CY = "Cyprus"
    CZ = "Czech Republic"
    DK = "Denmark"
    DJ = "Djibouti"
    DM = "Dominica"
    DO = "Dominican Republic"
    EC = "Ecuador"
    EG = "Egypt"
    SV = "El Salvador"
    GQ = "Equatorial Guinea"
    ER = "Eritrea"
    EE = "Estonia"
    ET = "Ethiopia"
    FK = "Falkland Islands (Malvinas)"
    FO = "Faroe Islands"
    FJ = "Fiji"
    FI = "Finland"
    FR = "France"
    GF = "French Guiana"
    PF = "French Polynesia"
    TF = "French Southern Territories"
    GA = "Gabon"
    GM = "Gambia"
    GE = "Georgia"
    DE = "Germany"
    GH = "Ghana"
    GI = "Gibraltar"
    GR = "Greece"
    GL = "Greenland"
    GD = "Grenada"
    GP = "Guadeloupe"
    GU = "Guam"
    GT = "Guatemala"
    GN = "Guinea"
    GW = "Guinea-Bissau"
    GY = "Guyana"
    HT = "Haiti"
    HM = "Heard and Mc Donald Islands"
    VA = "Holy See (Vatican City State)"
    HN = "Honduras"
    HK = "Hong Kong"
    HU = "Hungary"
    IS = "Iceland"
    IN = "India"
    ID = "Indonesia"
    IR = "Iran (Islamic Republic of)"
    IQ = "Iraq"
    IE = "Ireland"
    IL = "Israel"
    IT = "Italy"
    JM = "Jamaica"
    JP = "Japan"
    JO = "Jordan"
    KZ = "Kazakhstan"
    KE = "Kenya"
    KI = "Kiribati"
    KP = "Korea Democratic People's Republic of"
    KR = "Korea Republic of"
    KW = "Kuwait"
    KG = "Kyrgyzstan"
    LA = "Lao People's Democratic Republic"
    LV = "Latvia"
    LB = "Lebanon"
    LS = "Lesotho"
    LR = "Liberia"
    LY = "Libyan Arab Jamahiriya"
    LI = "Liechtenstein"
    LT = "Lithuania"
    LU = "Luxembourg"
    MO = "Macau"
    MK = "Macedonia The Former Yugoslav Republic of"
    MG = "Madagascar"
    MW = "Malawi"
    MY = "Malaysia"
    MV = "Maldives"
    ML = "Mali"
    MT = "Malta"
    MH = "Marshall Islands"
    MQ = "Martinique"
    MR = "Mauritania"
    MU = "Mauritius"
    YT = "Mayotte"
    MX = "Mexico"
    FM = "Micronesia Federated States of"
    MD = "Moldova Republic of"
    MC = "Monaco"
    MN = "Mongolia"
    MS = "Montserrat"
    MA = "Morocco"
    MZ = "Mozambique"
    MM = "Myanmar"
    NA = "Namibia"
    NR = "Nauru"
    NP = "Nepal"
    NL = "Netherlands"
    AN = "Netherlands Antilles"
    NC = "New Caledonia"
    NZ = "New Zealand"
    NI = "Nicaragua"
    NE = "Niger"
    NG = "Nigeria"
    NU = "Niue"
    NF = "Norfolk Island"
    MP = "Northern Mariana Islands"
    NO = "Norway"
    OM = "Oman"
    PK = "Pakistan"
    PW = "Palau"
    PA = "Panama"
    PG = "Papua New Guinea"
    PY = "Paraguay"
    PE = "Peru"
    PH = "Philippines"
    PN = "Pitcairn"
    PL = "Poland"
    PT = "Portugal"
    PR = "Puerto Rico"
    QA = "Qatar"
    RE = "Reunion"
    RO = "Romania"
    RF = "Russian Federation"
    RU = "Russia"
    RW = "Rwanda"
    KN = "Saint Kitts and Nevis"
    LC = "Saint LUCIA"
    VC = "Saint Vincent and the Grenadines"
    WS = "Samoa"
    SM = "San Marino"
    ST = "Sao Tome and Principe"
    SA = "Saudi Arabia"
    SN = "Senegal"
    SC = "Seychelles"
    SL = "Sierra Leone"
    SG = "Singapore"
    SK = "Slovakia (Slovak Republic)"
    SI = "Slovenia"
    SB = "Solomon Islands"
    SO = "Somalia"
    ZA = "South Africa"
    GS = "South Georgia and the South Sandwich Islands"
    ES = "Spain"
    LK = "Sri Lanka"
    SH = "St. Helena"
    PM = "St. Pierre and Miquelon"
    SD = "Sudan"
    SR = "Suriname"
    SJ = "Svalbard and Jan Mayen Islands"
    SZ = "Swaziland"
    SE = "Sweden"
    CH = "Switzerland"
    SY = "Syrian Arab Republic"
    TW = "Taiwan Province of China"
    TJ = "Tajikistan"
    TZ = "Tanzania United Republic of"
    TH = "Thailand"
    TG = "Togo"
    TK = "Tokelau"
    TO = "Tonga"
    TT = "Trinidad and Tobago"
    TN = "Tunisia"
    TR = "Turkey"
    TM = "Turkmenistan"
    TC = "Turks and Caicos Islands"
    TV = "Tuvalu"
    UG = "Uganda"
    UA = "Ukraine"
    AE = "United Arab Emirates"
    GB = "United Kingdom"
    US = "United States"
    UM = "United States Minor Outlying Islands"
    UY = "Uruguay"
    UZ = "Uzbekistan"
    VU = "Vanuatu"
    VE = "Venezuela"
    VN = "Viet Nam"
    VG = "Virgin Islands (British)"
    VI = "Virgin Islands (U.S.)"
    WF = "Wallis and Futuna Islands"
    EH = "Western Sahara"
    YE = "Yemen"
    ZM = "Zambia"
    ZW = "Zimbabwe"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
