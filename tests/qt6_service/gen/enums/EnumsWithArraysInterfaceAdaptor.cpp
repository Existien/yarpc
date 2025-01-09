/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/06.2_enums_with_arrays.yml
 *   Object: EnumsWithArrays
 *   Template: qt6/service_source.j2
 */
#include "EnumsWithArraysInterfaceAdaptor.hpp"

using namespace gen::enums;

EnumsWithArraysInterfaceAdaptor::EnumsWithArraysInterfaceAdaptor(EnumsWithArraysInterface* iface, QObject* parent) : m_iface(iface), QDBusAbstractAdaptor(parent) {

}

QList<int> EnumsWithArraysInterfaceAdaptor::EnumMethod(
    QList<int> color,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleEnumMethodCalled(_message);
    return {};
}

QList<int> EnumsWithArraysInterfaceAdaptor::getEnumProperty() const {
    auto value = m_iface->getEnumProperty();
    return *reinterpret_cast<const QList<int>*>(&value);
}

void EnumsWithArraysInterfaceAdaptor::setEnumProperty(const QList<int> &value ) {
    emit m_iface->propertyEnumPropertySet(*reinterpret_cast<const QList<Color::Type>*>(&value));
}

