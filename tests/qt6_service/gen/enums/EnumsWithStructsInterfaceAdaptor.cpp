/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/06.4_enums_with_structs.yml
 *   Object: EnumsWithStructs
 *   Template: qt6/service_source.j2
 */
#include "EnumsWithStructsInterfaceAdaptor.hpp"

using namespace gen::enums;

EnumsWithStructsInterfaceAdaptor::EnumsWithStructsInterfaceAdaptor(EnumsWithStructsInterface* iface, QObject* parent) : m_iface(iface), QDBusAbstractAdaptor(parent) {

}

EnumStruct EnumsWithStructsInterfaceAdaptor::EnumMethod(
    EnumStruct color,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleEnumMethodCalled(_message);
    return {};
}

EnumStruct EnumsWithStructsInterfaceAdaptor::getEnumProperty() const {
    auto value = m_iface->getEnumProperty();
    return value;
}

void EnumsWithStructsInterfaceAdaptor::setEnumProperty(const EnumStruct &value ) {
    emit m_iface->propertyEnumPropertySet(value);
}

