from signal_ocean.util.parsing_helpers import _to_snake_case

from signal_ocean.scraped_positions import ScrapedPosition


def test_positions_field_names():
    api_fields = [
        "PositionID",
        "MessageID",
        "ParsedPartID",
        "LineFrom",
        "LineTo",
        "Source",
        "UpdatedDate",
        "ReceivedDate",
        "IsDeleted",
        "ScrapedVesselName",
        "ScrapedDeadweight",
        "ScrapedYearBuilt",
        "IMO",
        "VesselName",
        "Deadweight",
        "YearBuilt",
        "LiquidCapacity",
        "VesselTypeID",
        "VesselType",
        "VesselClassID",
        "VesselClass",
        "ScrapedOpenDate",
        "OpenDateFrom",
        "OpenDateTo",
        "ScrapedOpenPort",
        "OpenGeoID",
        "OpenName",
        "OpenTaxonomyID",
        "OpenTaxonomy",
        "ScrapedCommercialOperator",
        "CommercialOperatorID",
        "CommercialOperator",
        "ScrapedCargoType",
        "CargoTypeID",
        "CargoType",
        "CargoTypeGroupID",
        "CargoTypeGroup",
        "ScrapedLastCargoTypes",
        "LastCargoTypesIDs",
        "LastCargoTypes",
        "HasBallast",
        "HasDryDock",
        "HasIf",
        "HasOnHold",
        "HasOnSubs",
        "HasPrompt",
        "HasUncertain",
        "IsPositionList",
        "Content",
        "Sender",
        "IsPrivate",
    ]
    snake_case_api_fields = list(map(_to_snake_case, api_fields))
    scraped_positions_model_fields = list(ScrapedPosition.__dataclass_fields__)
    assert snake_case_api_fields == scraped_positions_model_fields
