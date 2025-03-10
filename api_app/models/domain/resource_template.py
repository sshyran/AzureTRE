from typing import Dict, Any, List, Optional

from pydantic import Field

from models.domain.azuretremodel import AzureTREModel
from models.domain.resource import ResourceType


class Property(AzureTREModel):
    type: str = Field(title="Property type")
    title: str = Field("", title="Property description")
    description: str = Field("", title="Property description")
    default: Any = Field(None, title="Default value for the property")
    enum: Optional[List[str]] = Field(None, title="Enum values")
    const: Optional[Any] = Field(None, title="Constant value")
    multipleOf: Optional[float] = Field(None, title="Multiple of")
    maximum: Optional[float] = Field(None, title="Maximum value")
    exclusiveMaximum: Optional[float] = Field(None, title="Exclusive maximum value")
    minimum: Optional[float] = Field(None, title="Minimum value")
    exclusiveMinimum: Optional[float] = Field(None, title="Exclusive minimum value")
    maxLength: Optional[int] = Field(None, title="Maximum length")
    minLength: Optional[int] = Field(None, title="Minimum length")
    pattern: Optional[str] = Field(None, title="Pattern")
    updateable: Optional[bool] = Field(None, title="Indicates that the field can be updated")
    readOnly: Optional[bool] = Field(None, title="Indicates the field is read-only")
    items: Optional[dict] = None  # items can contain sub-properties


class CustomAction(AzureTREModel):
    name: str = Field(None, title="Custom action name")
    description: str = Field("", title="Action description")


class PipelineStepProperty(AzureTREModel):
    name: str = Field(title="name", description="name of the property to update")
    type: str = Field(title="type", description="data type of the property to update")
    value: str = Field(title="value", description="value to use in substitution for the property to update")


class PipelineStep(AzureTREModel):
    stepId: Optional[str] = Field(title="stepId", description="Unique id identifying the step")
    stepTitle: Optional[str] = Field(title="stepTitle", description="Human readable title of what the step is for")
    resourceTemplateName: Optional[str] = Field(title="resourceTemplateName", description="Name of the template for the resource under change")
    resourceType: Optional[ResourceType] = Field(title="resourceType", description="Type of resource under change")
    resourceAction: Optional[str] = Field(title="resourceAction", description="Action - install / upgrade / uninstall etc")
    properties: Optional[List[PipelineStepProperty]]


class Pipeline(AzureTREModel):
    install: Optional[List[PipelineStep]]
    upgrade: Optional[List[PipelineStep]]
    uninstall: Optional[List[PipelineStep]]


class ResourceTemplate(AzureTREModel):
    id: str
    name: str = Field(title="Unique template name")
    title: str = Field("", title="Template title or friendly name")
    description: str = Field(title="Template description")
    version: str = Field(title="Template version")
    resourceType: ResourceType = Field(title="Type of resource this template is for (workspace/service)")
    current: bool = Field(title="Is this the current version of this template")
    type: str = "object"
    required: List[str] = Field(title="List of properties which must be provided")
    properties: Dict[str, Property] = Field(title="Template properties")
    actions: List[CustomAction] = Field(default=[], title="Template actions")
    customActions: List[CustomAction] = Field(default=[], title="Template custom actions")
    pipeline: Optional[Pipeline] = Field(default=None, title="Template pipeline to define updates to other resources")

    # setting this to false means if extra, unexpected fields are supplied, the request is invalidated
    additionalProperties: bool = Field(default=False, title="Prevent unspecified properties being applied")
