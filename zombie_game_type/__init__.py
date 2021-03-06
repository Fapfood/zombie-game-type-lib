from .service import *

resource_static_service = ResourceService()
resource_pack_static_service = ResourcePackService(resource_static_service)
resource_drop_probability_static_service = ResourceDropProbabilityService(resource_static_service)

skill_static_service = SkillService()
skill_level_static_service = SkillLevelService(skill_static_service)
skill_pack_static_service = SkillPackService(skill_level_static_service)

production_static_service = ProductionService(skill_pack_static_service, resource_pack_static_service)
building_category_static_service = BuildingCategoryService()
building_room_static_service = BuildingRoomService(building_category_static_service, production_static_service)

zone_room_category_static_service = ZoneRoomCategoryService()
zone_room_action_static_service = ZoneRoomActionService()
zone_room_filler_static_service = ZoneRoomFillerService(zone_room_category_static_service,
                                                        resource_drop_probability_static_service,
                                                        zone_room_action_static_service)

zone_category_static_service = ZoneCategoryService()
zone_room_blank_static_service = ZoneRoomBlankService(zone_room_category_static_service)
zone_frame_static_service = ZoneFrameService(zone_category_static_service,
                                             zone_room_blank_static_service)
