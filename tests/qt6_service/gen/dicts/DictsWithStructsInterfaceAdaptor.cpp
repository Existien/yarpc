/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/05.2_dictionaries_with_structs.yml
 *   Object: DictsWithStructs
 *   Template: qt6/service_source.j2
 */
#include "DictsWithStructsInterfaceAdaptor.hpp"

using namespace gen::dicts;

DictsWithStructsInterfaceAdaptor::DictsWithStructsInterfaceAdaptor(DictsWithStructsInterface* iface, QObject* parent) : m_iface(iface), QDBusAbstractAdaptor(parent) {

}

QMap<QString, SimonsDict> DictsWithStructsInterfaceAdaptor::DictsStructMethod(
    QMap<QString, StructDict> numbers,
    const QDBusMessage &_message
){
    _message.setDelayedReply(true);
    m_iface->handleDictsStructMethodCalled(_message);
    return {};
}

QMap<QString, StructDict> DictsWithStructsInterfaceAdaptor::getDictStructProperty() const {
    auto value = m_iface->getDictStructProperty();
    return value;
}

void DictsWithStructsInterfaceAdaptor::setDictStructProperty(const QMap<QString, StructDict> &value ) {
    emit m_iface->propertyDictStructPropertySet(value);
}

