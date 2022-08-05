from signal_ocean.util.parsing_helpers import _to_snake_case

from signal_ocean.scraped_cargoes import ScrapedCargo


def test_cargoes_field_names():
    api_fields = [
        "CargoID",
        "MessageID",
        "ParsedPartID",
        "LineFrom",
        "LineTo",
        "InLineOrder",
        "Source",
        "UpdatedDate",
        "ReceivedDate",
        "IsDeleted",
        "ScrapedLaycan",
        "LaycanFrom",
        "LaycanTo",
        "ScrapedLoad",
        "LoadGeoID",
        "LoadName",
        "LoadTaxonomyID",
        "LoadTaxonomy",
        "ScrapedLoad2",
        "LoadGeoID2",
        "LoadName2",
        "LoadTaxonomyID2",
        "LoadTaxonomy2",
        "ScrapedDischarge",
        "ScrapedDischargeOptions",
        "DischargeGeoID",
        "DischargeName",
        "DischargeTaxonomyID",
        "DischargeTaxonomy",
        "ScrapedDischarge2",
        "DischargeGeoID2",
        "DischargeName2",
        "DischargeTaxonomyID2",
        "DischargeTaxonomy2",
        "ScrapedCharterer",
        "ChartererID",
        "Charterer",
        "ScrapedCargoType",
        "CargoTypeID",
        "CargoType",
        "CargoTypeGroupID",
        "CargoTypeGroup",
        "ScrapedQuantity",
        "Quantity",
        "QuantityBuffer",
        "QuantityFrom",
        "QuantityTo",
        "SizeFrom",
        "SizeTo",
        "ScrapedDeliveryDate",
        "DeliveryDateFrom",
        "DeliveryDateTo",
        "ScrapedDeliveryFrom",
        "DeliveryFromGeoID",
        "DeliveryFromName",
        "DeliveryFromTaxonomyID",
        "DeliveryFromTaxonomy",
        "ScrapedDeliveryTo",
        "DeliveryToGeoID",
        "DeliveryToName",
        "DeliveryToTaxonomyID",
        "DeliveryToTaxonomy",
        "ScrapedRedeliveryFrom",
        "RedeliveryFromGeoID",
        "RedeliveryFromName",
        "RedeliveryFromTaxonomyID",
        "RedeliveryFromTaxonomy",
        "ScrapedRedeliveryTo",
        "RedeliveryToGeoID",
        "RedeliveryToName",
        "RedeliveryToTaxonomyID",
        "RedeliveryToTaxonomy",
        "CharterTypeID",
        "CharterType",
        "CargoStatusID",
        "CargoStatus",
        "Content",
        "Sender",
        "IsPrivate",
    ]
    snake_case_api_fields = list(map(_to_snake_case, api_fields))
    scraped_cargoes_model_fields = list(ScrapedCargo.__dataclass_fields__)
    assert snake_case_api_fields == scraped_cargoes_model_fields
