"""Singer schema for Offer objects."""

from singer_sdk import typing as th

schema = th.PropertiesList(
    th.Property("id", th.IntegerType),
    th.Property("version", th.IntegerType),
    th.Property("application_id", th.IntegerType),
    th.Property("job_id", th.IntegerType),
    th.Property("candidate_id", th.IntegerType),
    th.Property(
        "opening",
        th.ObjectType(
            th.Property("id", th.IntegerType),
            th.Property("opening_id", th.StringType),
            th.Property("status", th.StringType),
            th.Property("opened_at", th.DateTimeType),
            th.Property("closed_at", th.DateTimeType, required=False),
            th.Property("application_id", th.IntegerType, required=False),
            th.Property(
                "close_reason",
                th.ObjectType(
                    th.Property("id", th.IntegerType),
                    th.Property("name", th.StringType),
                ),
            ),
        ),
    ),
    th.Property("created_at", th.StringType),
    th.Property("updated_at", th.StringType),
    th.Property("sent_at", th.StringType),
    th.Property("resolved_at", th.StringType),
    th.Property("starts_at", th.StringType),
    th.Property("status", th.StringType),
    th.Property(
        "custom_fields",
        th.ObjectType(
            th.Property("employment_type", th.StringType, required=False),
            th.Property("favorite_station", th.StringType, required=False),
            th.Property("best_seasons", th.StringType, required=False),
            th.Property("start_date", th.StringType, required=False),
            th.Property("willing_to_negotiate", th.StringType, required=False),
            th.Property("salary", th.IntegerType, required=False),
            th.Property("notes", th.StringType, required=False),
            th.Property("location", th.StringType, required=False),
            th.Property("compensation", th.StringType, required=False),
            th.Property("equity", th.StringType, required=False),
            th.Property("sign_on_bonus_incentive", th.StringType, required=False),
            th.Property("relocation_bonus", th.StringType, required=False),
            th.Property("leveling_at_offer", th.StringType, required=False),
            th.Property("years_of_exp_at_offer", th.StringType, required=False)

        ),
    ),
    th.Property(
        "keyed_custom_fields",
        th.ObjectType(
            th.Property(
                "time_type",
                th.ObjectType(
                    th.Property("name", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("value", th.StringType),
                ),
            ),
            th.Property(
                "favorite_station",
                th.ObjectType(
                    th.Property("name", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("value", th.StringType),
                ),
            ),
            th.Property(
                "best_seasons",
                th.ObjectType(
                    th.Property("name", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("value", th.StringType, required=False),
                ),
            ),
            th.Property(
                "start_date",
                th.ObjectType(
                    th.Property("name", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("value", th.StringType),
                ),
            ),
            th.Property(
                "will_negotiate",
                th.ObjectType(
                    th.Property("name", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("value", th.StringType, required=False),
                ),
            ),
            th.Property(
                "salary",
                th.ObjectType(
                    th.Property("name", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("value", th.StringType),
                ),
            ),
            th.Property(
                "notes",
                th.ObjectType(
                    th.Property("name", th.StringType),
                    th.Property("type", th.StringType),
                    th.Property("value", th.StringType),
                ),
            ),
        ),
    ),
)

schema_dict = schema.to_dict()
